#!/usr/bin/python3
import math
import sys, re, os, random, subprocess


def test_premier(n):
	#renvoie True si n premier, False sinon
	if n == 2:
		return True
	if n%2 == 0:
		return False
	if n%3 == 0:
		return False
	if n%5 == 0:
		return False
	#on enlève les cas du début 
	k = int(math.sqrt(n)) + 1
	for i in range(7,k):
		if n %k == 0:
			return False
	return True

def pgcd(a, b): #on a ainsi: x*a + b*y = gcd
	x,y, u,v=0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v= a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def nombre_premier(n):
	n_0=random.choice('1379')
	n_max=random.choice('123456789')

	n_i=n_0

	for i in range(1,n-1):
		n_i=n_i+random.choice('0123456789')
	
	n_i=n_i+n_max
	p=int(n_i)

	commande=subprocess.run("openssl prime %d 2> /dev/stdout"%p, shell=True, stdout=subprocess.PIPE)
	mon_exp_reguliere=re.compile(r"is not prime")

	resultat=mon_exp_reguliere.search(str(commande))

	while(resultat):
		n_i=n_i[1:]+random.choice('0123456789')+random.choice('1379')
		p=int(n_i)
		commande=subprocess.run("openssl prime %d 2> /dev/stdout"%p, shell=True, stdout=subprocess.PIPE)
		resultat=mon_exp_reguliere.search(str(commande))
	return p


def modinv(a, m):
	gcd, x, y = pgcd(a, m)
	if gcd != 1:
		return None
	return x % m

def decoupage(message, l):
	#fonctions pour découper un message en morceaux de longueur l
	#problème si len(message) n'est pas multiple de l
	n = len(message)
	if n%l !=0:
		message = message + (l - n%l)*"X" #padding avec des X
		n = n + l - n%l
	Liste_message = []
	q = n//l
	for i in range(q):
		Liste_message.append(message[i*l : l+i*l])
	return Liste_message

def chiffrage(message,e,n):
	M=message.encode('utf-8')
	C=int.from_bytes(M, byteorder='big')
	C = powmod(C,e,n)
	C=C.to_bytes(C.bit_length()//8 + 1, byteorder='big')
	return C

def dechiffrage(chiffre,d,n):
	m = int.from_bytes(chiffre,byteorder='big')
	clair = powmod(m, d, n)
	clair = clair.to_bytes(m.bit_length()//8+1, byteorder='big')
	clair=clair.decode('utf-8','ignore')
	return clair
	
def powmod(x,y,m): #calcule x**y mod m
	a=1
	while y>0:
		if y&1>0:
			a = (a*x) % m
		y >>=1 
		x = (x*x) % m
	return a
