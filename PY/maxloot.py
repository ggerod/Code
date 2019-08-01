#!/usr/bin/python3


itemarray = [[24,3],[28,4],[30,5]]
print(itemarray)

for item in itemarray:
    item.append(item[0]/item[1])

print(itemarray)

spacelimit=9
itemstotake=[]

for item in itemarray:
    if (spacelimit >= item[1]):   # there is space for it all
        itemstotake.append(item)
        spacelimit -= item[1]
    else:   # there is only space for some
        itemstotake.append([spacelimit*item[2],spacelimit,spacelimit*item[2]/spacelimit])
        spacelimit = 0
    if (spacelimit == 0):
        break

print("items to take>>")
print(itemstotake)

