#!/usr/bin/python3

#-*- coding:utf-8 -*-
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import trace




print("Hello world!\nVous avez lancé le logiciel de test de connexion des serveur sur le réseau!")


os.chdir("/home/sellig/")  #move to the folder containing the list / délacement dans le dossier contenant la liste
				
with open("test_python.txt","r") as ma_liste:    #retrieval and testing of elements from a pre-established list: / récupération et test des éléments d'une liste pré-établie: 
    texte = ma_liste.read()
    print(texte)
    ma_liste1 = texte.split()
    rec2 = len(ma_liste1)
    print(rec2)
with open("data.html","w") as code_html:                #creating an html file / création d' un fichier html
    code_html.write("""
        <html>
        <head>
        <meta charset="utf-8" />
        </head>
        <body>
""")

x = 0

while x != rec2 :               #ping + traceroute the list's addresses and write the result to the html file / ping + traceroute des addresses de la liste  et écriture 							     #du résultat dans le fichier html
    rep = os.system("ping -c 1 " + ma_liste1[x])
    rep1 = os.system("traceroute " + ma_liste1[x] +" > trace.txt")
    with open("trace.txt","r") as trace:
        traceroute = trace.read()
    if rep == 0:
        ma_liste2 = open("data.html","a")
        ma_liste2.write("\n" + "<p>&emsp;&emsp;serveur &emsp;&emsp;-------->&emsp;&emsp;" + ma_liste1[x] + "&emsp;&emsp;-------->&emsp;&emsp;" "<font color='green'> Connecté </font>&emsp;&emsp;<br>" + traceroute + "</br></p>")    
    else:
        ma_liste2 = open("data.html","a")
        ma_liste2.write("\n" + "<p>&emsp;&emsp;serveur &emsp;&emsp;-------->&emsp;&emsp;"+ ma_liste1[x] + "&emsp;&emsp;-------->&emsp;&emsp;" "<font color='red'> Déconnecté </font>&emsp;&emsp;<br>" + traceroute + "</br></p>")

    time.sleep(3)
    ma_liste2.close()
    x = x+1
    
with open("data.html","a") as code_html_fin:            #end code of the html file / code de fin du fichier html
    code_html_fin.write(""" 
    </body>
    </html>

""")
with open("data.html","r") as data:                 #Sending the html file by mail / Envoi du fichier html par mail
    final = data.read()


server = smtplib.SMTP()                     #Connection to the server and information useful information / connection au serveur et renseignement des informations utiles.
server.connect("smtp.gmail.com", 587)
server.starttls()
server.login("LOGIN SENDBOX" , "PASSWORD")
fromaddr= "EMAIL SENDBOX"
toaddr="EMAIL RECEPTION","AUTRE EMAIL DE RECEPTION"

sujet = "RAPPORT QUOTIDIEN"

html = final

msg = MIMEMultipart("alternative")  #element information variables requested from an email in html format / variables de renseignements des éléments demandé d' un email sous 							#format html
msg["Subject"] = sujet
msg["From"] = fromaddr
msg["To"] = ",".join(toaddr)
part = MIMEText(html, "html")
msg.attach(part)
try:                                                            # conformity test / test de conformité.
    server.sendmail(fromaddr, toaddr, msg.as_string())
except smtplib.SMTPException as e:                              #Recuperation of errors / récuprération des erreurs
        print(e)

server.quit()

print("fin")
