#!/usr/bin/python3

def calc_fib(n):
    fb=[0,1]
    if (n<2):
        return n
    for i in range(2,n+1):
        fb.append(fb[i-2] + fb[i-1])
    return(fb.pop())

n = int(input("nth Fibonacci number to calculate:"))
assert(n>=0)
print(calc_fib(n))

