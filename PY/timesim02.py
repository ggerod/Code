#!/usr/bin/python3
import random
import statistics


timecounts=[]
simcount=0

while (simcount < 10000):
    #roll = random.choice(range(0,899))
    roll = 899
    timecounts.append(roll)
    simcount+=1


#print(timecounts)
print("length>>")
print(len(timecounts))
print("min >>")
print(min(timecounts))
print("max >>")
print(max(timecounts))
print("average >>")
print(statistics.mean(timecounts))
print()
print("progression>>")
for i in range(len(timecounts)):
    bestest = ((900 *(i+1)) + timecounts[i])/(i+1)
    print((i+1),bestest)
