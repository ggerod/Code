#!/usr/bin/python3
import subprocess
import gmpy2
from gmpy2 import mpz

N =mpz(648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877)

rtN = gmpy2.isqrt(N)

cnt=0
pct=0
# Find A upward from rtN within 2**20 digits.  
for dist in range(1,1048577):
    cnt += 1
    if (cnt == 10485):
        curtime = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print("time is", curtime)
        cnt = 0
        pct += 1
        print("pct done = ",pct)

    A = mpz(rtN + dist)

    # x = sqrt((A**2) - N)
    A2 = A ** 2
    x = gmpy2.isqrt(A2 - N)

    # p = A-x (test for prime)
    p = A - x
    if not (gmpy2.is_prime(p)):
        continue

    # q = A+x (test for prime)
    q = A + x
    if not (gmpy2.is_prime(q)):
        continue

    # check if p*q = N
    Ntest = gmpy2.mul(p,q)
    if (Ntest == N):
        print("N = ", N)
        print("p = ", p)
        print("q = ", q)
        print("pq= ", Ntest)
        break
