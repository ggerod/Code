#!/usr/bin/python3
# Find the smallest number that is evenly divisible by all factors from 1-20

# can start at 20
numtocheck = 20 

while (True):
    #can jump by 20 each time
    numtocheck += 20

    #print status
    if (numtocheck % 15000000 == 0):
        print("chcking :",numtocheck)

    # go backwards for speed only have to go to 11
    for factor in range(19, 10, -1):
        if (numtocheck % factor != 0):
            break
        if (factor == 11):
            # we have an answer
            print("the answer is: ",numtocheck)
            exit()
