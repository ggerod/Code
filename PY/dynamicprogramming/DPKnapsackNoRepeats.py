#!/usr/bin/python3


def PrintArray():
    for i in range(NumItems+1):
        for j in range(maxweighttocheck+1):
            tn=str(KValues[i][j])
            tn = '0'*(2-len(tn))+tn
            print(tn," ",end="")
        print()
    print()


# Items[i] = [weight,value]
Items=[[6,30],[3,14],[4,16],[2,9]]
NumItems=len(Items)
maxweighttocheck=10

KValues=[[0 for j in range(maxweighttocheck+1)] for i in range(NumItems+1)]
PrintArray()

for item in range(1,NumItems+1):
    for weight in range(maxweighttocheck+1):
        KValues[item][weight] = KValues[item-1][weight]
        if (Items[item-1][0] <= weight):
            value = KValues[item-1][weight-(Items[item-1][0])] + Items[item-1][1]
            if (KValues[item][weight] < value):
                KValues[item][weight] = value
        PrintArray()
