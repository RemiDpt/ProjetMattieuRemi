#!/usr/bin/python3
import math
import sys, re, os


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
	k = int(math.sqrt(n)) + 1
	for i in range(7,k):
		if n %k == 0:
			return False
	return True

print(test_premier(341))