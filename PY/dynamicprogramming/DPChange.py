#!/usr/bin/python3

#coins=[1,2,3,6]
#coins=[1,3,4]
coins=[1,5,10,25,50]
maxvaltocheck=1000

MinNumCoins=[0]

for val in range(1,maxvaltocheck+1):
    MinNumCoins.append(-1)
    for j in range(len(coins)):
        if (val >= coins[j]):
            mincoins = MinNumCoins[val-coins[j]] + 1
            if ((MinNumCoins[val] == -1) or (mincoins < MinNumCoins[val])):
                MinNumCoins[val] = mincoins

print("coins = ",coins)
print("MinNumCoins = ",MinNumCoins)
