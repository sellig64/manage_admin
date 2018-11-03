# task_auto_python_admin
Hi everybody, sorry for my English,

--- This script ping servers via a file containing multiple IP addresses (one per line) and send a report email.

--- this script is created with the use of a gmail account in the outbox (SMTP server 'gmail' in this example).

Configuration:

1) Make sure the "Allow less secure apps" tab is enabled in your Google Account (URL: https://myaccount.google.com/security).

2) create a file named "text_python.txt" or modify the code line 19 to change the name, insert the ip address of your servers (one per line) and indicate the address of the file on line 17.

3) Indicate the address of the desired SMTP server and its port on line 63.

4) Indicate the login and password of your email account on line 65.

5) Indicate the sending email line 66.

6) Indicate the receipt (s) line (s) in line 67 in quotation marks and separated by commas.

7) Line 69 will be the title message of the mail, to modify if you want.

------------------------------------------------------------------------------------------------------
--- ce script envoie une requête ping à des serveurs via un fichier contenant plusieurs adresses IP (une par ligne) et envoie un e-mail de rapport.

--- ce script est créé avec l'utilisation d'un compte gmail dans la boîte d'envoi (serveur SMTP 'gmail' dans cet exemple).

Configuration:

1) Assurez-vous que l'onglet "Autoriser les applications moins sécurisées" est activé dans votre compte Google (URL: https://myaccount.google.com/security).

2) créer un fichier nommé "text_python.txt" ou modifier le code ligne 19 pour changer le nom, y déposer l'adresse ip de vos serveurs (une par ligne) et indiquer l'adresse du fichier à la ligne 17.

3) Indiquer l'adresse du serveur smtp souhaité ainsi que son port à la ligne 63.

4) Indiquer le login et le mot de passe de votre compte mail à la ligne 65.

5) Indiquer l'email d'envoi ligne 66.

6) Indiquer le ou les emails de réception(s) ligne 67 entre guillemets et séparé par des virgules.

7) La ligne 69 sera le message d'intitulé du mail, à modifier si vous voulez.
