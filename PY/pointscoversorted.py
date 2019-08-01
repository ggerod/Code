#!/usr/bin/python3
import gmpy2
from gmpy2 import mpz


def findseg(points):
    seg=[points[0],points[0]+2]
    points = [p for p in points if p > seg[1]]
    return(points,seg)


points = [2,2,3,5,5,6,7,8,8,8,11,15]
segs=[]
while (len(points) > 0):
    points,newseg=findseg(points)
    segs.append(newseg)
print(segs)
