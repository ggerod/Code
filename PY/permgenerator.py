#!/usr/bin/pypy3

#blist = [1,2,2,4,5]
blist = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3]

blist.sort()
lastindex=(len(blist))
pointer = lastindex-2
print(blist)
while (True):
    # look at digits to right of pointer
    maxtoright = max(blist[pointer+1:lastindex])
    if (maxtoright > blist[pointer]):
        # if any are larger than the digit at pointer, take the smallest of them, and switch with 
        # digit at pointer.   Sort the rest to the right of the pointer.  Print
        testamt = blist[pointer]
        while (True):
            testamt += 1
            if (testamt in blist[pointer+1:lastindex]):
                switchindex = ((blist[pointer+1:lastindex]).index(testamt) + pointer +1)
                tmp = blist[pointer]
                blist[pointer] = blist[switchindex]
                blist[switchindex] = tmp
                tl = (blist[pointer+1:lastindex])
                tl.sort()
                blist = blist[0:pointer+1] + tl
                print(blist)
                break
        pointer = lastindex-2
    else:
        # if no digits to the right are strictly larger than digit at pointer, move pointer left one spot.
        # repeat until you finish pointer at index 0
        pointer -= 1
        if (pointer == -1):
            exit(0)
