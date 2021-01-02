#!/usr/bin/python3

import socket, sys, os

adresse_ip = 'localhost'
porc = 9997
temps_attente = 15 #nombre de secondes d'attente de connexion 


socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) # ouverture du socket
socquette.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socquette.bind((adresse_ip, porc)) 
socquette.listen(temps_attente) #attente de connexion

connexion, TSAP_depuis = socquette.accept()

while True:
	truc=input("Appuyer sur entrée pour accepter : \n")
	print("Nouvelle connexion depuis : " , TSAP_depuis)
	truc=truc.encode('utf-8')
	connexion.sendall(truc)
	#connexion.close()
	reponse=connexion.recv(255)
	if reponse !="":
		print (reponse)
socquette.close()
