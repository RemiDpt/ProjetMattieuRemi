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
		S.append(u)
	for i in range(len(S)):
		if (S[i]<100):
			S[i] +=900
		S[i]=str(S[i])
	print(S)
	X = ''.join(S)
	print(X)
	X = bytes(str(powmod(int(X),e,n)),'utf-8')
	return X

def nouv_dech(bitbit,d,n):
	X = int(bitbit.decode('utf-8'))
	X = str(powmod(X,d,n))
	print(X)
	M = decoupage(X,3)
	print(M)
	for i in range(len(M)):
		M[i] = int(M[i])
		if (M[i]>=900):
			M[i] -= 900
	MesFin = (bytes(M)).decode('utf-8')
	return MesFin

message = "mon cochon marche au plafond"
PO = decoupage(message,3)

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