#!/usr/bin/python3
import subprocess
import gmpy2
from gmpy2 import mpz

N =mpz(720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929)

pcheck=mpz(21909849592475533092273988531583955898982176093344929030099423584127212078126069429518044884213613626482058256336732179043313827449665449729331360356980944)
q=mpz(32864774388713299638410982797375933848473264140017393545149135376190818117189360958630403025071010379594201403056648830209031486655099285772544447003230479)


rt6N = gmpy2.isqrt(6*N)
A = mpz(rt6N)

# x = sqrt((A**2) - 6N)
A2 = A ** 2
#x = (gmpy2.isqrt(A2 - (6*N))) -2


# Find p upward from 
for dist in range(1,1048577):

    pcheck = gmpy2.next_prime(pcheck)

    # pcheck (test for prime)
    if not (gmpy2.is_prime(pcheck)):
        continue

    # qcheck = N/pcheck (test for remainder and prime)
    (qcheck,r) = gmpy2.f_divmod(N,pcheck)
    if not (r == 0):
        continue

    # check if p*q = N
    Ntest = gmpy2.mul(pcheck,qcheck)
    if (Ntest == N):
        print("N = ", N)
        print("p = ", pcheck)
        print("q = ", qcheck)
        print("pq= ", Ntest)
        break
