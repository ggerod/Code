#!/usr/bin/python3


OnesCount=[0 for i in range(11)]

for i in range(1024):
    bn=format(i,"b")
    bn='0'*(10-len(bn)) + bn
    #print(bn)
    NumArray=[]
    for c in bn:
        NumArray.append(int(c))
    numones=NumArray.count(1)
    OnesCount[numones]+=1

total=0
for i in range(11):
    total+=OnesCount[i]
    print(i,OnesCount[i],"p=",OnesCount[i]/1024)

print()
print("total =",total)
