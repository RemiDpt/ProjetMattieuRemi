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
		socquette.sendall(bytes(message))
		cle = socquette.recv(1024)
		if not cle:
			break
		nb = int(cle)
		print ("la clé de Bob est n = ", nb, "\n")
		cpt += 1
	else:
		truc=''
		i=0
		M =(input("Saisissez votre message : \n"))
		while (i) !=(len(decoupage(M,2))):
			C=chiffrage(decoupage(M,2)[i],e,nb)
			socquette.sendall(bytes(C))
			reponse=socquette.recv(1024)
			if reponse!="":
				truc=truc+dechiffrage(reponse,d,na)
				#print(reponse,"Reçu")
				#print("Déchiffrage :")
				#print (dechiffrage(reponse,d,na))
				#print("\n")
			i=i+1
		print("déchiffrageidgnruiofqi")
		print(truc)
	#message = (input("Entrez un message à envoyer\n")).encode("utf-8")
	
socquette.close()
