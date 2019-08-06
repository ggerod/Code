#!/usr/bin/python3
import sys

numcases = int(sys.stdin.readline())

for casenum in range(numcases):
    print("Case #"+str(casenum+1)+": ",end="")
    checkamt = (sys.stdin.readline()).rstrip()
    checkamt = str(int(checkamt))
    newamt1 = int(checkamt)
    newamt2 = 0
    ndigm1 = len(checkamt)-1

    for i in range(ndigm1,-1,-1):
        if ((int(checkamt[i])) == 4):
            newamt1 -= (10 ** (ndigm1-i))
            newamt2 += (10 ** (ndigm1-i))

    print(str(newamt1)+" "+str(newamt2))
