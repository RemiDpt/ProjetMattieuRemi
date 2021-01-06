#!/usr/bin/python3


import socket, sys, os, time
from fonctions_projet import *

adresse_serveur = socket.gethostbyname('localhost')
porc = 8790
socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socquette.connect((adresse_serveur, porc))
except Exception as e:
	print("On a un problème", e.args)
	sys.exit(1)

taille_min_premier  = 50

print("Génération des clefs en cours ...\n")

t1 = time.time()
p = nombre_premier(taille_min_premier)
q = nombre_premier(taille_min_premier)
na = p * q
phi_n = (p-1) * (q-1)
e = 65537
d = modinv(e, phi_n)
t2 = time.time()

print("Clefs générées en ", t2-t1, " secondes. \n")

cpt = 0

while True:
	if cpt == 0:
		cle = str(na).encode('utf-8')
		socquette.send(bytes(cle))
		print("En attente de la clef... \n")
		cle = socquette.recv(1024)
		if not cle:
			break
		nb = int(cle)
		print ("la clé de Bob est n = ", nb, "\n")
		cpt += 1
	else:
		print("\nBob écrit ...\n")
		reponse=socquette.recv(1024)
		if reponse == b'':
			print("Bob ne veut plus vous parler :( \n")
			break
		elif reponse != '':
			print("Le chiffré est : ",reponse, "\n")
			Mes = nouv_dech(reponse,d,na)
			print("Le clair est : ",Mes,"\n")
		M =(input("Saisissez votre message : (Appuyer sur entrée pour quitter)\n"))
		if(M==""):
			print("\nConnexion interrompue : Ciao Bob. \n")
			break
		C = nouv_chif(M,e,nb)
		socquette.send(bytes(C))
		
	
	
	
socquette.close()
