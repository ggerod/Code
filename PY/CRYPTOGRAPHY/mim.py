#!/usr/bin/python3
import subprocess
import gmpy2
from gmpy2 import mpz

p=mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
g=mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
h=mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')
B=mpz(2 ** 20)
ans=mpz('0')
denom=mpz('0')
side1={}

pct=0
cnt=0
#for x1 in range(0,10):
for x1 in range(0,1048577):
    # compute the denominator
    denom = gmpy2.f_mod((g ** x1),p)

    # find inverse of g ** x1
    inv=pow(denom,p-2,p)

    # multiply inverse of g ** x1 by h
    ans = gmpy2.mul(h,inv)

    # find modulus of this result
    ans2 = gmpy2.f_mod(ans,p)

    # hash the result
    side1[ans2] = x1

    #print("denom = ",denom)
    #print("inv = ",inv)
    #print("inv * denom % p  = ",(inv * denom) % p)
    #print("ans = ",ans)
    #print("ans2 = ",ans2)
    #print(side1.keys())
    #print("-------------------------------------------------")
    cnt += 1
    if (cnt == 10485):
        curtime = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print("time is", curtime)
        cnt = 0
        pct += 1
        print("pct done = ",pct,"  -  size of hash = ",len(side1))


print("len side1 = ", len(side1))
#print(side1[mpz(4199087091266497145601348207583924848226517492270490701972381723726933114421087716583962101410861186664491712311297804186703238635304249772231592850914292)])
print("====================Half 1 done========================")
cnt=0
pct=0
for x0 in range(0,1048577):
    cnt += 1
    if (cnt == 10485):
        curtime = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print("time is", curtime)
        cnt = 0
        pct += 1
        print("pct done = ",pct)

    # compute g ** (B * x0)
    exponent = gmpy2.mul(B, x0)
    value = gmpy2.powmod(g, exponent, p)

    # See if that value is in the hash table
    if (value in side1):
        print("WE HAVE A MATCH")
        print("x0 = ",x0)
        print("x1 = ",side1[value])
        print("matching value = ", value)
        break




