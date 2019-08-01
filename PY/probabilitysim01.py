#!/usr/bin/python3
import random
import statistics


rollcounts=[]
simcount=0

while (simcount < 1000000):
    rolls=0
    set=[0,0,0,0,0,0]

    while (0 in set):
        roll = random.choice(range(0,6))
        rolls+=1
        set[roll]=1

    rollcounts.append(rolls)
    simcount+=1


#print(rollcounts)
print("length>>")
print(len(rollcounts))
print("min >>")
print(min(rollcounts))
print("max >>")
print(max(rollcounts))
print("average >>")
print(statistics.mean(rollcounts))
