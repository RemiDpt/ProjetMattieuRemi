#!/usr/bin/python3

import sys
import subprocess
import random
import re

random.seed()

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
	
def pgcd(a, b):
	x,y, u,v=0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v= a,r, u,v, m,n
	gcd = b
	return gcd, x, y
	
def modinv(a, m):
	gcd, x, y = pgcd(a, m)
	if gcd != 1:
		return None
	return x % m


p=nombre_premier(5)
q=nombre_premier(8)
print(p)
print(q)

n=p*q
phi_n=(p-1)*(q-1)

