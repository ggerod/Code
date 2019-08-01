#!/usr/bin/python3

def switch(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


pat=[2,4,6,2,65,4,12,4,62,16,2,31,886,42,646,8,4,22,42,114]
print(pat)

#selection sort >>
for i in range(len(pat)):
    lowindex=i
    for j in range(i+1,len(pat)):
        if (pat[j] < pat[lowindex]):
            lowindex = j
    switch(pat,i,lowindex)

print(pat)
