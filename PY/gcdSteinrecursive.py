#!/usr/bin/python3

def st_gcd(u,v):
    if (u == v):
        return(u)

    if (u == 0):
        return(v)

    if (v == 0):
        return(u)

    # look for factors of 2
    if (~u & 1): # u is even
        if (v & 1): # v is odd
            return(st_gcd(u >> 1, v))
        else: # both u and v are even
            return(st_gcd(u >> 1, v >> 1) << 1)

    if (~v & 1): # u is odd, v is even
        return(st_gcd(u, v >> 1))

    # both odd
    # reduce larger argument
    if (u > v):
        return(st_gcd((u - v) >> 1, v))

    return(st_gcd((v - u) >> 1, u))


a, b = map(int,input("Enter two numbers for gcd:").split())
print("gcd of ",a,"and",b,"is: ",end="")
print(st_gcd(a,b))
