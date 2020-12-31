#!/usr/bin/python3

import sys
import subprocess
import random
import re
from fonctions_projet import *

random.seed()

#On choisit p et q premiers pour calculer n
#on a de base e = 65 537
#on recherche inverse de e mod (p-1)(q-1)
e = 65537
p=nombre_premier(5)
q=nombre_premier(8)
print(p)
print(q)

n=p*q
phi_n=(p-1)*(q-1)

#Alice envoie n et e à Bob
cle_pub = (e, n)
cle_priv = (e , d)


M = 55551
#Bob utilise e pour chiffrer M

C = powmod(M,e,n)
#Bob envoie C à Alice

#Alice calcule l'inverse de e mod phi_n
d = modinv(e, phi_n)

#Alice peut déchiffrer le message de Bob
DM = powmod(C,d,n)


