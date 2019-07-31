#!/usr/local/bin/python3
from itertools import permutations

permstring = "glengerod"

#print(permstring)

perms = permutations(permstring)

for perm in list(perms):
#	print(perm)
	print("".join(perm))
