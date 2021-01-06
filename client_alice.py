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
	print("Connexion...")
	message = str(n).encode('utf-8')
	socquette.sendall(bytes(message))
	data=socquette.recv(1024)
	if not data:
		break	
	trad.append(nouv_dech(bytes(data,"utf-8"),d,n))
	trad=[]
	for j in range(len(mes)):
		trad.append(nouv_dech(bytes(mes[j],"utf-8"),d,n))
	
socquette.close()
