#!/usr/local/bin/python3

num = int(input("Enter max number to generate multiplication table: "))

for x in range(-1,num+1):
	for y in range(-1,num+1):
		if ((x==-1) and (y==-1)):
			print("  X", end=" ")
			continue
		print("%3d" % abs(x*y), end=" ")
	print()
