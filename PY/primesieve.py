#!/usr/local/bin/python3
import gmpy2
from gmpy2 import mpz


#maxnum=int(input("Prime check maximum number:"))
maxnum=100000
nums=[i for i in range(2,maxnum+1)]
maxcheck = gmpy2.isqrt(maxnum)

for num in nums:
    if (num > maxcheck):
        break
    i=2
    while ((num * i) <= nums[-1]):
        if ((num * i) in nums):
            nums.pop(nums.index((num * i)))
        i+=1

print("Primes up to:",maxnum)
print(nums)
