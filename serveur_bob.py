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
cpt = 0
p = nombre_premier(3)
q = nombre_premier(4)
nb= p * q
phi_n = (p-1) * (q-1)
e = 65537
d = modinv(e, phi_n)
truc=''
while True:
	if cpt == 0:
		print("Premiere connexion depuis : " , TSAP_depuis)
		cle=connexion.recv(1024)
		na= int(cle.decode('utf-8'))
		if cle !="":
			print ("la clé de Alice est n = ", na, "\n")
			mes=str(nb).encode('utf-8')
			connexion.sendall(bytes(mes))
			cle=connexion.recv(1024)
			cpt += 1
	else:
		truc=''
		i=0
		M =(input("Saisissez votre message : \n"))
		while (i) !=(len(decoupage(M,2))):
			C=chiffrage(decoupage(M,2)[i],e,na)
			connexion.sendall(bytes(C))
			reponse=connexion.recv(1024)
			if reponse !="":
				#print(reponse)
				truc=truc+dechiffrage(reponse,d,nb)
			#print("Déchiffrage : \n")
			#print (truc)
			i=i+1
		print("déchifehziuoidjziopjdkoz")
		print(truc)
		
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
