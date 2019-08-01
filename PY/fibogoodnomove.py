#!/usr/bin/python3
#
# Juice not worth the squeeze.  Takes one minute longer to compute fib(10000000) = 19.5 minutes

def calc_fib(n):
    fib=[0,1,1]
    if (n<2):
        return n
    for i in range(2,n+1):
        fib[i%3]=fib[(i+1)%3]+fib[(i+2)%3]
    return(fib[i%3])

n = int(input("nth Fibonacci number to calculate:"))
assert(n>=0)
print(calc_fib(n))
