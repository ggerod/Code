#!/usr/bin/python3

def calc_fib(n):
    fbmin1=0
    fbnew=1
    if (n<2):
        return n
    for i in range(2,n+1):
        fbmin2 = fbmin1
        fbmin1 = fbnew
        fbnew = fbmin2 + fbmin1
    return(fbnew)

n = int(input("nth Fibonacci number to calculate:"))
assert(n>=0)
print(calc_fib(n))

