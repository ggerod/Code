#!/usr/bin/python3

def switchthem(i,j):
    ltmp=lol[i]
    lol[i]=lol[j]
    lol[j]=ltmp


def findlowest(loi):
    for i in range(loi+1,len(lol)):
        if (int(lol[i][0]) < int(lol[loi][0])):
            #switch them
            switchthem(loi,i)
        elif (int(lol[i][0]) == int(lol[loi][0])):
            #check 2nd index
            if (int(lol[i][1]) < int(lol[loi][1])):
                #switch them
                switchthem(loi,i)
            elif (int(lol[i][1]) == int(lol[loi][1])):
                #check 3rd index
                if (int(lol[i][2]) < int(lol[loi][2])):
                    #switch them
                    switchthem(loi,i)


lol=[]
with open('revinput', 'r') as f:
    for line in f:
        line=line.rstrip()
        lst=line.split('.')
        lol.append(lst)

loindex=0
while (loindex < len(lol)-1):
    findlowest(loindex)
    loindex+=1

print("sorted >>>")
for lst in lol:
    print(lst)
