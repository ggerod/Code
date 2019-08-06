#!/usr/local/bin/python3
import sys

numcases = int(sys.stdin.readline())

for casenum in range(numcases):
    print("Case #"+str(casenum+1)+": ",end="")
    gridsize = int((sys.stdin.readline()).rstrip())
    movelist = ((sys.stdin.readline()).rstrip())

    if (movelist[-1] == "E"): moves=["E","S"]
    else: moves=["S","E"]

    #if the field is clear mark the breakthru point
    if (movelist[0] == moves[1]):
        BTP=0
    else:     #else find where to break through
        btind=movelist.find(moves[1]+moves[1])
        BTP=movelist.count(moves[1],0,btind) + 1

    #now move to the break thru point
    firstmoves = moves[1]*BTP
    print(firstmoves,end="")

    # now break all the way through
    secondmoves = moves[0]*(gridsize - 1)
    print(secondmoves,end="")

    # now go to the finish line
    lastmoves = moves[1] * (gridsize - BTP -1)
    print(lastmoves)
