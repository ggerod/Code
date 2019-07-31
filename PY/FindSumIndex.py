#!/usr/local/bin/python3
from random import randint
sumnumber=100

a=[]
for i in range(201):
	a.append(randint(1,100))
print(a)

	
for startindex in range(0,len(a)-1):
	for checkindex in range(startindex+1,len(a)):
		if (a[startindex] + a[checkindex] == sumnumber):
			print("index[",startindex,"] (",a[startindex],") + index[",checkindex,"](",a[checkindex],") = ",sumnumber)
