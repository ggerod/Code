#!/usr/bin/python3

def swap(a,b):
    temp = pat[a]
    pat[a] = pat[b]
    pat[b] = temp


def partition(p,r):
    if (r-p > 0):
        q=p
        for i in range(p,r):
            if (pat[i] <= pat[r]):
                swap(i,q)
                q+=1
        swap(r,q)
        arraysubsets.append([p,q-1])
        arraysubsets.append([q+1,r])


pat=[2,4,6,2,65,4,12,4,62,16,2,31,886,42,646,8,4,22,42,114]
print(pat)

#iterative quick sort >>
arraysubsets=[]
arraysubsets.append([0,len(pat)-1])

while (len(arraysubsets) > 0):
    subsettowork=arraysubsets.pop()
    partition(subsettowork[0],subsettowork[1])

print(pat)
