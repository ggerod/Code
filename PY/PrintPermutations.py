#!/usr/local/bin/python3
from itertools import permutations

permstring = input("Enter string to permute: ")
permstring = permstring.strip(' ')
permstring = permstring.replace(" ","")

#print(permstring)

perms = permutations(permstring)

for perm in list(perms):
#	print(perm)
	print("".join(perm))
