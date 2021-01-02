#!/usr/bin/python3


import socket, sys, os
from fonctions_projet import *

adresse_serveur = socket.gethostbyname('localhost')
porc = 8790
socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socquette.connect((adresse_serveur, porc))
except Exception as e:
	print("On a un problème", e.args)
	sys.exit(1)


p = nombre_premier(3)
q = nombre_premier(4)
na= p * q
phi_n = (p-1) * (q-1)
e = 65537
d = modinv(e, phi_n)
cpt = 0



while True:
	if cpt == 0:
		print("Connexion...")
		message = str(na).encode('utf-8')
		socquette.send(bytes(message))
		cle = socquette.recv(1024)
		if not cle:
			break
		nb = int(cle)
		print (cle,"la clé de Bob est n = ", nb, "\n")
		cpt += 1
	else:
		M =(input("Saisissez votre message : \n"))
		C=chiffrage(M,e,nb)
		socquette.send(bytes(C))
		reponse=socquette.recv(1024)
		if reponse != '':
			print(reponse,"Reçu\n")
			print("Déchiffrage :", dechiffrage(reponse,d,na), "\n")
	#message = (input("Entrez un message à envoyer\n")).encode("utf-8")
	
socquette.close()
