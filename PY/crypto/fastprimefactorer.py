#!/usr/local/bin/python3
import gmpy2
from gmpy2 import mpz

import primelist1M
numberinput = input("what number do you want to factor into primes? : ")
numtofactor = mpz(numberinput)
print()
print("The number:",numtofactor)
print("has prime factors:")
print("[",end="")


def findprimefactor(numtofactor):
    for primenum in primelist1M.primelist:
        if (gmpy2.c_mod(numtofactor,primenum) == 0):
            return(primenum)
    return(0)


while(True):
    if gmpy2.is_prime(numtofactor):
        # We are done.  All prime factors found
        print(str(numtofactor)+"]")
        exit(0)

    primefactor = findprimefactor(numtofactor)

    if (primefactor == 0):
        # The remainder is not itself prime, and
	# has no factors in the prime list.
	# continue the 'hard way', maybe rho algorithm
        print("rem="+str(numtofactor)+"]")
        exit(0)

    print(str(primefactor)+",",end="")
    numtofactor = gmpy2.c_div(numtofactor,primefactor)
    #print("new num to factor = ",numtofactor)
