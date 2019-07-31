#!/usr/local/bin/python3

def customgen(s,n):
     num = s
     while (n > 0):
             yield num
             num*=s
             n -= 1

seed = int(input("Enter the nuber you wish to use as a seed: "))
lsize = int(input("Enter size of array to generate: "))
result = customgen(seed,lsize)

print(list(result))
