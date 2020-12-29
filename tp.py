#!/usr/bin/python3

import sys
import subprocess
import random
import re
from fonctions_projet import *

random.seed()

p=nombre_premier(5)
q=nombre_premier(8)
print(p)
print(q)

n=p*q
phi_n=(p-1)*(q-1)

mes = "turlututu chapeau pointu"
print((decoupage(mes,7)))

for i in range (len(decoupage(mes,7))):
	print(chiffrage((decoupage(mes,7)[i]),n))
	
print(powmod(45,3,78))

