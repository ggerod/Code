#!/usr/bin/python3


def exponent(num,expo):
    if (expo==0):
        return(1)
    if (expo%2 == 0):
        y=exponent(num,expo/2)
        return(y*y)
    else:
        y=exponent(num,expo-1)
        return(num * y)


NUM=12
EXPO=25
answer=exponent(NUM,EXPO)
print(NUM,"**",EXPO,"=",answer)
