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
n= p * q
phi_n = (p-1) * (q-1)
e = 65537
d = modinv(e, phi_n)
cpt = 0



while True:
	if cpt == 0:
		message = str(n).encode('utf-8')
		socquette.sendall(bytes(message))
		chiffre = socquette.recv(1024)
		if not chiffre:
			break
		print(chiffre, 'Reçu')
		m = int.from_bytes(chiffre,byteorder='big')
		print(m)
		clair = powmod(m, d, n)
		clair = clair.to_bytes(m.bit_length()//8+1, byteorder='big')
		clair=clair.decode()
		print(clair)
		cpt += 1
	#message = (input("Entrez un message à envoyer\n")).encode("utf-8")
	

socquette.close()
