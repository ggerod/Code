#!/usr/local/bin/python3

def customgen(n):
     xm2=0
     xm1=1
     while (n > 0):
             x=xm2+xm1
             yield xm1
             xm2 = xm1
             xm1 = x
             n -= 1

lsize = int(input("Enter size of array to generate: "))
result = customgen(lsize)

print(list(result))
