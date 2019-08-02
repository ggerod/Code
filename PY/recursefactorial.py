#!/usr/bin/python3


def fact(n):
    if ((n==0) or (n==1)):
        return(1)
    else:
        ans=n*fact(n-1)
        return(ans)

NUM=50
answer=fact(NUM)
print(NUM,"! =",answer)
