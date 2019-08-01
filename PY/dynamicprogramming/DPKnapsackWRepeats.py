#!/usr/bin/python3

# items[i] = [weight,value]
items=[[6,30],[3,14],[4,16],[2,9]]
maxweighttocheck=100000

MaxVals=[0]

for weight in range(1,maxweighttocheck+1):
    MaxVals.append(0)
    for i in range(len(items)):
        if ( items[i][0] <= weight ):
            value = MaxVals[weight-items[i][0]] + items[i][1]
            if (value > MaxVals[weight]):
                MaxVals[weight] = value

print("maxvals[",maxweighttocheck," = ",MaxVals[maxweighttocheck])
