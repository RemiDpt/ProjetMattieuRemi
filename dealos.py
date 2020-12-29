#!/usr/bin/python3

import socket, sys, os

adresse_ip = 'localhost'
porc = 9999
temps_attente = 15 #nombre de secondes d'attente de connexion 


socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) # ouverture du socket
socquette.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socquette.bind((adresse_ip, porc)) 
socquette.listen(temps_attente)#attente de connexion


while True:
	connexion, TSAP_depuis = socquette.accept()
	print("Nouvelle connexion depuis : " , TSAP_depuis)
	connexion.sendall(b'Yo le rap\n')
	connexion.close()

socquette.close()