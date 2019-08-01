#!/usr/bin/python3
import sys
sys.setrecursionlimit(100000)

# items[i] = [weight,value]
items=[[6,30],[3,14],[4,16],[2,9]]
maxweighttocheck=100000
MaxVals={}

def Knapsack(weight):
    if (weight in MaxVals):
        return(MaxVals[weight]) 
    MaxVals[weight] = 0
    for i in range(len(items)):
        if ( items[i][0] <= weight ):
            value = Knapsack(weight-items[i][0]) + items[i][1]
            if (value > MaxVals[weight]):
                MaxVals[weight] = value
    return(MaxVals[weight]) 



print("maxval(",maxweighttocheck,") = ",Knapsack(maxweighttocheck))
