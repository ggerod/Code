#!/usr/local/bin/python3
import gmpy2
from gmpy2 import mpz

def euc_gcd(a,b):
    while (b!=0):
        t=a
        a=b
        b=t%b
    return(a)


numtofactor = int(input("Enter number to factor: "))

x = 2
y = 2
factor = 1

while (factor == 1):
    x = (x*x + 1) % numtofactor
    y = (y*y + 1) % numtofactor
    y = (y*y + 1) % numtofactor
    factor = euc_gcd(abs(x-y), numtofactor)

if (factor == numtofactor):
    print("Fail")
else:
    print("A factor of that number is:",factor)
