#!/usr/bin/python3

n = int(input())
a = [int(x) for x in input().split()]
print("len a =",len(a))
print("n = ",n)
print("a = ",a)
assert(len(a) == n)

result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)
