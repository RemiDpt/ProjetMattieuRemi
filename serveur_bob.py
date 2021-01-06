#!/usr/bin/python3

import socket, sys, os
from fonctions_projet import *

adresse_ip = 'localhost'
port = 8790
temps_attente = 15 #nombre de secondes d'attente de connexion 
e = 65537


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
			n = int(cle)
			print ("la clé de Alice est n = ", n, "\n")		
			M =(input("Saisissez votre message : \n"))
			chiffre = nouv_chif(M,e,n)
			connexion.send(chiffre)
			cpt += 1
			break
		break
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
