# task_auto_python_admin             

# for all suggestions : bibi@gmail.com
Hi everybody, sorry for my English,

--- This script sends a ping + a traceroute + a port scan to servers via a file containing multiple IP addresses (one per line) and sends a report email while creating a replacement server.

--- This script is created with the use of a gmail account in the outbox (SMTP server 'gmail' in this example).

--- This script works on Debian type servers.

--- This script requires the installation of vitualbox and the creation of virtual machine of the same OS as the server to be replaced with an opening of user account, automatic and the basic pre-installation of the services concerned by each server as well as the creation of a functional backup and authorizing connection to the root account via ssh connecting with pre-configured ssh keys.

Configuration:

1) Make sure the "Allow less secure apps" tab is enabled in your Google Account (URL: https://myaccount.google.com/security).

2) indicate when running the script the name of the backup virtual machine and its ip address line 14 and 16.

3) indicate the path where the server backup is in .tar.gz format line 19 and 20

4) create a file named "test_python.txt" or modify the code line 29 to change the name, insert the ip address of your servers (one per line) and indicate the address of the file on line 27.

5) Indicate the address of the desired SMTP server and its port on line 81.

6) Indicate the login and password of your email account on line 83.

7) Indicate the sending email line 84.

8) Indicate the receipt (s) line (s) in line 85 in quotation marks and separated by commas.

9) Line 87 will be the title message of the mail, to modify if you want.

------------------------------------------------------------------------------------------------------
Bonjour à tous,                 
# pour toutes les suggestions : bibi@gmail.com
--- ce script envoie une requête ping + un traceroute + un nmap à des serveurs via un fichier contenant plusieurs adresses IP (une par ligne) et envoie un e-mail de rapport tout en créant un serveur de remplacement.

--- ce script est créé avec l'utilisation d'un compte gmail dans la boîte d'envoi (serveur SMTP 'gmail' dans cet exemple).

--- ce script fonctionne sur les serveurs type debian.

--- ce script nécessite l'installation de virtualbox et la créaton de machine virtuelle du même OS que le serveur à remplacer avec une ouverture de compte utilisateur automatique et la pré-installation de base des services concernés par chaque serveur ainsi que la création d'une backup fonctionnelle et de l'autorisation de connection au compte root via ssh se connectant avec des clés ssh pré-configurées.

Configuration:

1) Assurez-vous que l'onglet "Autoriser les applications moins sécurisées" est activé dans votre compte Google (URL: https://myaccount.google.com/security).

2) indiquer lors de l'execution du script le nom de la machine virtuelle de secours et son adresse ip ligne 14 et 16.

3) indiquer le chemin où se situe la sauvegarde du serveur au format .tar.gz ligne 19 et 20

4) Créer un fichier nommé "test_python.txt" ou modifier le code ligne 29 pour changer le nom, y déposer l'adresse ip de vos serveurs (une par ligne) et indiquer l'adresse du fichier à la ligne 27.

5) Indiquer l'adresse du serveur smtp souhaité ainsi que son port à la ligne 81.

6) Indiquer le login et le mot de passe de votre compte mail à la ligne 83.

7) Indiquer l'email d'envoi ligne 84.

8) Indiquer le ou les emails de réception(s) ligne 85 entre guillemets et séparé par des virgules.

9) La ligne 87 sera le message d'intitulé du mail, à modifier si vous voulez.
