#!/usr/bin/python3

alpha="abcdefghijklmnopqrstuvwxyz"
code1="gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
code2="vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"

for i in range(23,24):
    for letter in code2:
        #print(letter," - ",alpha.index(letter)," - ",alpha[alpha.index(letter) + 1])
        newindex=(alpha.index(letter) + i) % 26
        print(alpha[newindex], end="")
    print("---")

print("=========")

for i in range(19,20):
    for letter in code1:
        #print(letter," - ",alpha.index(letter)," - ",alpha[alpha.index(letter) + 1])
        newindex=(alpha.index(letter) + i) % 26
        print(alpha[newindex], end="")
    print("---")

