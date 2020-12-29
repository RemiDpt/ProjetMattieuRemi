#!/usr/bin/python3


import socket, sys, os

adresse_serveur = socket.gethostbyname('localhost')
porc = 9999
socquette = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socquette.connect((adresse_serveur, porc))
except Exception as e:
	print("On a un problème", e.args)
	sys.exit(1)

while True : 
    message = input("Entrez un message à envoyer\n").encode("utf-8")
    socquette.sendall(bytes(message))
    data = socquette.recv(1024)
    if not data:
    	break
    print(data, 'Reçu')

socquette.close()