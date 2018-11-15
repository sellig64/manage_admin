#!/usr/bin/python3

#-*- coding:utf-8 -*-
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import trace


def check_serveur():                        #Launch function of a backup virtual server / fonction de lancement d'un serveur virtuel de secour
    print("ERROR : Un serveur ne répond pas, entrez le nom de votre serveur fantôme à lancer : ")
    fantome = input()   
    print("Entrez l'IP de se serveur : ")
    virtual_ip = input()    
    os.system("vboxmanage startvm "+ fantome )
    time.sleep(60)
    os.system("cd /home/sellig/serveur_backup/ ")
    os.system("scp -r /home/sellig/serveur_backup/"+ ma_liste1[x] + ".tar.gz root@" + virtual_ip + ":/ ")
    os.system("ssh root@" + virtual_ip+ " ' sleep 30 && cd / && tar -xvpzf " + ma_liste1[x] + ".tar.gz -C / && reboot'")
    
    
print("Hello world!\nVous avez lancé le logiciel de test de connexion des serveurs sur le réseau!")


os.chdir("/home/sellig/")  #move to the folder containing the list / délacement dans le dossier contenant la liste

with open("test_python.txt","r") as ma_liste:   #retrieval and testing of elements from a pre-established list: / récupération et test des éléments d'une liste pré-établie:
    texte = ma_liste.read()
    print(texte)
    ma_liste1 = texte.split()
    rec2 = len(ma_liste1)
    print( rec2 )
with open("data.html","w") as code_html:        #creating an html file / création d' un fichier html
    code_html.write("""
        <html>
        <head>
        <meta charset="utf-8" />
        </head>
        <body>
""")

x = 0

while x != rec2 :   #ping + traceroute + nmap the list's addresses and write the result to the html file / ping + traceroute + nmap des addresses de la liste  et écriture 
    rep = os.system("ping -c 1 " + ma_liste1[x])
    rep1 = os.system("traceroute " + ma_liste1[x] +" > trace.txt")
    rep2 = os.system("nmap -Pn " + ma_liste1[x] + " > nmap.txt")
    
    with open("nmap.txt","r") as nmap:
        scanPort = nmap.read()
    
    with open("trace.txt","r") as trace:
        traceroute = trace.read()
    
    if rep == 0:
        ma_liste2 = open("data.html","a")
        ma_liste2.write("\n" + "<p>&emsp;&emsp;serveur &emsp;&emsp;-------->&emsp;&emsp;" + ma_liste1[x] + "&emsp;&emsp;-------->&emsp;&emsp;" "<font color='green'> Connecté </font>&emsp;&emsp;<br>""<font color='purple'> traceroute :</font> " + traceroute + "</br><br>""<font color='blue'> nmap : </font>" + scanPort + "</br></p>")    
    
    else:
        ma_liste2 = open("data.html","a")
        ma_liste2.write("\n" + "<p>&emsp;&emsp;serveur &emsp;&emsp;-------->&emsp;&emsp;"+ ma_liste1[x] + "&emsp;&emsp;-------->&emsp;&emsp;" "<font color='red'> Déconnecté </font>&emsp;&emsp;<br>""<font color='purple'> traceroute :</font>" + traceroute + "</br><br>""<font color='blue'> nmap : </font>" + scanPort + "</br></p>")   
        check_serveur()
        
    time.sleep(3)        
    x = x+1
    ma_liste2.close()
    
with open("data.html","a") as code_html_fin:            #end code of the html file / code de fin du fichier html
    code_html_fin.write(""" 
    </body>
    </html>

""")
with open("data.html","r") as data:                 #Sending the html file by mail / Envoi du fichier html par mail
    final = data.read()


server = smtplib.SMTP()         #Connection to the server and information useful information / connection au serveur et renseignement des informations utiles.
server.connect("smtp.gmail.com", 587)
server.starttls()
server.login("EMAIL SENDBOX" , "PASSWORD")
fromaddr= "EMAIL SENDBOX"
toaddr="EMAIL OF RECEPTION"

sujet = "RAPPORT QUOTIDIEN"

html = final        #element information variables requested from an email in html format / variables de renseignements des éléments demandé d' un email sous html

msg = MIMEMultipart("alternative")
msg["Subject"] = sujet
msg["From"] = fromaddr
msg["To"] = ",".join(toaddr)
part = MIMEText(html, "html")
msg.attach(part)
try:                    # conformity test / test de conformité.
    server.sendmail(fromaddr, toaddr, msg.as_string())
except smtplib.SMTPException as e:                              #Recuperation of errors / récuprération des erreurs
        print(e)

server.quit()

print("fin")
