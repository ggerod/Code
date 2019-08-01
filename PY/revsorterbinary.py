#!/usr/bin/python3

numlist=[]
with open('revinput', 'r') as f:
    for line in f:
        line=line.rstrip()
        lst=line.split('.')
        b1=format(int(lst[0]),'b')
        b1=((8-len(b1))*'0') + b1
        b2=format(int(lst[1]),'b')
        b2=((8-len(b2))*'0') + b2
        b3=format(int(lst[2]),'b')
        b3=((8-len(b3))*'0') + b3
        #print(b1)
        #print(b2)
        #print(b3)
        bignum=int(b1+b2+b3,2)
        #print(bignum)
        numlist.append(bignum)

numlist.sort()

#convert back to revision format >>
for num in numlist:
    binlong=format(int(num),'b')
    binlong=((24-len(binlong))*'0') + binlong
    #print(binlong)
    b1=binlong[0:8]
    b2=binlong[8:16]
    b3=binlong[16:24]
    print(int(b1,2),end=".")
    print(int(b2,2),end=".")
    print(int(b3,2))
