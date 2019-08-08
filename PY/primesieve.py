#!/usr/local/bin/python3
import math
import sys

#maxnum=int(input("Prime finder maximum number:"))
maxnum=1000000000

nindex = [1] * (maxnum+1)
primelist=[]

for i in range(2,int(math.sqrt(maxnum))+1):
    if (nindex[i]):
        for j in range(int(i*i),maxnum+1,i):
            nindex[j] = 0

print("Primes up to:",maxnum)
sys.stdout.write("[")
lb = 0
for i in range(2,maxnum+1):
    if (nindex[i]):
        sys.stdout.write(str(i)+",")
        lb += 1
        if (lb == 10):
            lb = 0
            print(' \\')
print("]")
