#!/usr/bin/python3
import gmpy2
from gmpy2 import mpz


points = [2,2,3,5,5,6,7,8,8,8,11,15]
segs=[]
index=0

while (index < len(points)):
    seg=[points[index],points[index]+2]
    segs.append(seg)
    while ((index < len(points)) and (points[index] < seg[1])):
        index+=1
print(segs)
