#!/usr/bin/python3
import math


def merge(B,C):
    D=[]
    while(1):
        if ((len(B) == 0) and (len(C) == 0)):
            break
        if (len(B) == 0):
            D.append(C.pop(0))
        elif (len(C) == 0):
            D.append(B.pop(0))
        else:
            if (B[0] < C[0]):
                D.append(B.pop(0))
            else:
                D.append(C.pop(0))
    return(D)


def mergesort(arr):
    if (len(arr) == 1):
        return(arr)
    mid=(math.floor(len(arr)/2))
    Barr=mergesort(arr[0:mid])
    Carr=mergesort(arr[mid:len(arr)])
    mergedarr = merge(Barr,Carr)
    return(mergedarr)
    


pat=[2,4,6,2,65,4,12,4,62,16,2,31,886,42,646,8,4,22,42,114]
print(pat)

#merge sort >>
pat2 = mergesort(pat)

print(pat2)
