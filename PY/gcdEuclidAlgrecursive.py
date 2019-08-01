#!/usr/bin/python3

def euc_gcd(a,b):
    if (b==0):
        return(a)
    return(euc_gcd(b,a%b))

print("Enter numbers to get gcd:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("gcd of ",a,"and",b,"is: ",end="")
print(euc_gcd(a,b))
