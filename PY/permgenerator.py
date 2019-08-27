#!/usr/bin/pypy3

#blist = [1,2,2,4,5]
blist = [0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3]

blist.sort()
lastindex=(len(blist)-1)
pointer = lastindex-1
print(blist)
while (True):
    #print("pointer = ",pointer)
    # look at digits to right of pointer
    maxtoright = max(blist[pointer+1:lastindex+1])
    #print("blist[pointer] = ",blist[pointer])
    #print("maxtoright = ",maxtoright)
    if (maxtoright > blist[pointer]):
        #print("inf if")
        # if any are larger than the digit at pointer, take the smallest of them, and switch with 
        # digit at pointer.   Sort the rest to the right of the pointer.  Print
        testamt = blist[pointer]
        while (True):
            testamt += 1
            if (testamt in blist[pointer+1:lastindex+1]):
                switchindex = ((blist[pointer+1:lastindex+1]).index(testamt) + pointer +1)
                #print("switchindex = ",switchindex)
                tmp = blist[pointer]
                blist[pointer] = blist[switchindex]
                blist[switchindex] = tmp
                #print(blist)
                #print(blist[0:pointer+1]) 
                #print(blist[pointer+1:lastindex+1])
                tl = (blist[pointer+1:lastindex+1])
                tl.sort()
                #print(tl)
                blist = blist[0:pointer+1] + tl
                print(blist)
                break
        pointer = lastindex-1
    else:
        #print("inf else")
        # if no digits to the right are strictly larger than digit at pointer, move pointer left one spot.
        # repeat until you finish pointer at index 0
        pointer -= 1
        #print("pointer = ",pointer)
        if (pointer == -1):
            exit(0)
