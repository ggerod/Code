#!/usr/bin/python3

def euc_gcd(a,b):
    while (b!=0):
        t=a
        a=b
        b=t%b
    return(a)


print("Enter numbers to get gcd:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("gcd of ",a,"and",b,"is: ",end="")
print(euc_gcd(a,b))
