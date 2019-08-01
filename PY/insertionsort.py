#!/usr/bin/python3

def insertinarray(arr,i):
    val = arr[i]
    j = i-1
    while ( j > 0 and arr[j] > val):
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = val


pat=[2,4,6,2,65,4,12,4,62,16,2,31,886,42,646,8,4,22,42,114]
print(pat)

#insertion sort >>
for i in range(1,len(pat)):
    insertinarray(pat,i)

print(pat)
