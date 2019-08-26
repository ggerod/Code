#!/usr/local/bin/python3


name=[
"",
"Thousand",
"Million",
"Billion",
"Trillion",
"Quadrillion",
"Quintillion",
"Sextillion",
"Septillion",
"Octillion",
"Nonillion",
"Decillion",
"Undecillion",
"Duodecillion",
"Tredecillion",
"Quattuordecillion",
"Quinquadecillion",
"Sedecillion",
"Septendecillion",
"Octodecillion",
"Novendecillion",
"Vigintillion" ]

n1= input("num: ")
if (len(n1)%3 > 0):
    n1 = ('0' * (3-(len(n1)%3))) + n1

tris=[n1[i:i+3] for i in range(0,len(n1)-2,3)]

for i in range(0,len(tris)):
    print(tris[i],end="")
    if(i != (len(tris)-1)):
        print(",",end="")
print()
print()

for i in range(0,len(tris)):
    print(tris[i]," ",end="")
    print(name[(len(tris)-i)-1])
