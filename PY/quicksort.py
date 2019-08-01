#!/usr/bin/python3


def swap(arr,n1,n2):
    temp=arr[n1]
    arr[n1]=arr[n2]
    arr[n2]=temp

def partition(arr,p,r):
    #print("in partition")
    q=p
    for j in range(p,r):
        if(arr[j] <= arr[r]):
            swap(arr,j,q)
            q+=1
    swap(arr,r,q)
    return(q)

def quicksort(arr,p,r):
    #print("do quicksort. p=",p,"r=",r)
    if ((r-p) > 0):
        q=partition(arr,p,r)
        #print("q=",q)
        #print(array)
        #print("do first half")
        quicksort(arr,p,q-1)
        #print("do second half")
        quicksort(arr,q+1,r)


array = [1,14,22,3,44,5,6,80,-4,5222,222,2,22,6,1268,-2357,33,28832,14,2,55,2,7,3,445,73,6]
print("before:")
print(array)
quicksort(array,0,(len(array)-1))
print("after:")
print(array)
