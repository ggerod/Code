#!/usr/local/bin/pypy3
import gmpy2
from gmpy2 import mpz


# 245634634573565468780056745643563568569345634576824563463457356546878005674564356356856934563457682456346345735654687800567456435635685693456345768
# Factors: 3,88,37,37,23,43,289,1933,2539,130099,63799,4715467,10838689,246091348709,267652966241599,2603941883787374089,
numtofactor = mpz(int(input("Enter number to factor: ")))
print("Factors: ",end="")

while (True):
    x = mpz(2)
    y = mpz(2)
    factor = mpz(1)

    while (factor == 1):
        x = gmpy2.mul(x,x)
        x = gmpy2.add(x,1)
        x = gmpy2.t_mod(x,numtofactor)
        y = gmpy2.mul(y,y)
        y = gmpy2.add(y,1)
        y = gmpy2.t_mod(y,numtofactor)
        y = gmpy2.mul(y,y)
        y = gmpy2.add(y,1)
        y = gmpy2.t_mod(y,numtofactor)
        factor = gmpy2.gcd(abs(gmpy2.sub(x,y)), numtofactor)

    if (factor == numtofactor):
        print("Fail.  Remaining number to factor = ",numtofactor)
        exit(1)
    else:
        print(str(factor)+",",flush=True,end="")
        numtofactor = gmpy2.c_divexact(numtofactor,factor)
        if gmpy2.is_prime(numtofactor):
            # We are done.  All prime factors found
            print(str(numtofactor)+"]")
            exit(0)
