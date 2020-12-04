#!/usr/bin/python3

import sys
import subprocess
import random
import re

random.seed()
n_0=random.choice('1379')
n_max=random.choice('123456789')

n_i=n_0
max=3

for i in range(1,max-1):
	n_i=n_i+random.choice('0123456789')
	
n_i=n_i+n_max
p=int(n_i)

commande=subprocess.run("openssl prime %d 2> /dev/stdout"%p, shell=True, stdout=subprocess.PIPE)
mon_exp_reguliere=re.compile(r"is not prime")

resultat=mon_exp_reguliere.search(str(commande))

while(resultat):
	n_i=n_i[1:]+random.choice('1379')
	p=int(n_i)
	commande=subprocess.run("openssl prime %d 2> /dev/stdout"%p, shell=True, stdout=subprocess.PIPE)
	resultat=mon_exp_reguliere.search(str(commande))
else:
	print("c'est un premier")
	print(n_i)
