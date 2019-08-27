#!/usr/bin/pypy3
from math import factorial


def nck(nn,kk):
    return(int(factorial(nn) / ((factorial(kk)) * factorial(nn-kk))))

n = 26
k = 63


keyspaceonemin = 0
for i in range(26):
    print(i,((-1)**i),nck(26,i),((26-i)**63))
    keyspaceonemin += (((-1)**i) * nck(26,i) * ((26-i)**63))

keyspacenomin = 26**63
print("The keyspace if there are no restrictions on the number of cyphertext symbols per Englisth letter is:")
print(keyspacenomin)
print(len(str(keyspacenomin)),"digits")

print("The keyspace if there must be at least one cyphertext symbol per Englisth letter is:")
print(keyspaceonemin)
#print(1 * (10**88))
print(len(str(keyspaceonemin)),"digits")
print("1.01 * 10**88")

