#!/usr/bin/python3

import socket, sys, os
from fonctions_projet import *

adresse_ip = 'localhost'
port = 8790
temps_attente = 15 #nombre de secondes d'attente de connexion 

taille_min_premier  = 50
e = 65537
p = nombre_premier(taille_min_premier)
q = nombre_premier(taille_min_premier)
nb= p * q
print("La clé est générée, Alice peut se connecter")
phi_n = (p-1) * (q-1)
d = modinv(e, phi_n)

socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) # ouverture du socket
socquette.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socquette.bind((adresse_ip, port)) 
socquette.listen(temps_attente) #attente de connexion

connexion, TSAP_depuis = socquette.accept()
cpt  = 0

while True:
	if cpt == 0:		
		print("Premiere connexion depuis : " , TSAP_depuis)
		cle = connexion.recv(1024)
		cle = cle.decode('utf-8')
		if cle !="":
			na = int(cle)
			print ("la clé de Alice est n = ", na, "\n")
			mes=str(nb).encode('utf-8')
			connexion.send(bytes(mes))
			cpt += 1		
			
	else:
		M =(input("Saisissez votre message : (Appuyer sur entrée pour quitter)\n"))
		if(M==""):
			break
		chiffre = nouv_chif(M,e,na)
		connexion.send(chiffre)
		reponse=connexion.recv(1024)
		if reponse != "":
			print("Le chiffré est : ",reponse, "\n")
			Mes = nouv_dech(reponse,d,nb)
			print("Le clair est : ",Mes,"\n")

connexion.close()



#connexion.close() # utile pour un seul échange






	#print("Premiere depuis : " , TSAP_depuis)
	#reponse=connexion.recv(1024)
	#reponse= reponse.decode('utf-8')
	#if reponse !="":
	#	n = int(reponse)
	#	print (reponse)
	#message=input("Saisissez votre réponse : \n")
	#message=message.encode('utf-8')
	#connexion.sendall(message)
	#connexion.close() # utile pour un seul échange
socquette.close()
