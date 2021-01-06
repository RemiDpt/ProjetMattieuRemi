#!/usr/bin/python3

import sys
import subprocess
import random
import re
from fonctions_projet import *

e = 65537
p = nombre_premier(2)
q = nombre_premier(2)
n = p * q
phi_n = (p-1) * (q-1)
d = modinv(e, phi_n)

def nouv_chif(chaine,e,n):
	S = []
	A = bytes(chaine,'utf-8')
	for u in A:
		S.append(u) #on place chaque octet de la chaine dans un tableau 
	for i in range(len(S)):
		if (S[i]<100):
			S[i] +=900 #on place des repères pour les nombres plus petits que 100
		S[i]=str(S[i]) #on concatène les éléments du tableau 
	X = ''.join(S)
	X = bytes(str(powmod(int(X),e,n)),'utf-8')
	return X

def nouv_dech(bitbit,d,n):
	X = int(bitbit.decode('utf-8'))
	X = str(powmod(X,d,n))
	M = decoupage(X,3) #on récupère toutes valeurs stockées lors du chiffrement
	for i in range(len(M)):
		M[i] = int(M[i])
		if (M[i]>=900):
			M[i] -= 900 #on retrouve les valeurs initialement <100
	print(M)
	MesFin = (bytes(M)).decode('utf-8')
	return MesFin

message = "tp de merde"
PO = decoupage(message,2)

P = bytes(message,'utf-8')
O = []
for u in P:
		O.append(u)

NPO = []
for i in range(len(PO)):
	NPO.append(nouv_chif(PO[i],e,n))

Z = []
for j in range(len(NPO)):
	Z.append(nouv_dech(NPO[j],d,n))
print("Z = : ",Z)
