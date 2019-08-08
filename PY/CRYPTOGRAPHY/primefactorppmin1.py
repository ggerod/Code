#!/usr/local/bin/python3
import gmpy2
from gmpy2 import mpz


def primes(n):
    ps = []
    sieve = [True] * int(n)
    for p in range(2,int(n)):
        if sieve[p]:
            ps.append(p)
            for i in range(p*p,n,p):
                sieve[i] = False
    return ps


def pminus1(n, b):
    c = mpz(2)
    for p in primelist:
        pp = p
        while pp < b:
            c = gmpy2.powmod(c, p, n)
            pp = pp * p
    g = gmpy2.gcd(c-1, n)
    #print("g = ",g)
    if (1 < g < n):
        return g
    return 1


numtofactor = mpz(int(input("Enter number to factor: ")))
bfac = mpz(int(input("Enter b: ")))
#numtofactor = 87463
#bfac = 120
print("Factors: [",end="")

primelist = primes(bfac)
#print("primelist = ",primelist)
while (True):
    if (numtofactor != 1): print("numtofactor = ",numtofactor)
    factor = pminus1(numtofactor,bfac)
    if gmpy2.is_prime(factor):
        print(str(factor)+",",flush=True,end="")
        numtofactor = gmpy2.divexact(numtofactor,factor)
        if gmpy2.is_prime(numtofactor):
            # We are done.  All prime factors found
            print(str(numtofactor)+"]")
            exit(0)
    else:
        realfactor = gmpy2.divexact(numtofactor,factor)
        print(str(realfactor)+",",flush=True,end="")
        numtofactor = factor
