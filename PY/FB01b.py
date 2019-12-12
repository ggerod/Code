#!/usr/local/bin/python3
# Consider a square grid of size N, where N>=3. I have placed a battleship of
# size 3 somewhere in the grid, and you want to sink my battleship by ordering
# the bombing of specified coordinates.
#
# The battleship can only be placed vertically or horizontally, not diagonally.
# Every coordinate which does not contain the battleship is empty. Your task is
# to write a function which takes as input N, and returns the 3 coordinates of
# the battleship.
#
# Assume you have a function, boolean bomb_location(x, y), which will return
# True if (x, y) "hits" the battleship and False if (x, y) misses the 
# battleship.
#
# For example - in the following grid your function find_battleship(grid_size),
# given grid_size of 8,  would return ((2,1), (2,2), (2,3)):
#
# * . . * . . * .
# . * X . * . . *
# . . * . . * . .
# * . X * . . * .
# . * . . * . . *
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .

def bomb_location(x,y):
    if ((x == 2) and (y in [1,2,3])): return True
    return False


def getFirstHit(N):
    i0=0
    j=0
    while (j < N):
        i = i0
        while (True):
            if (bomb_location(i,j)): return((i,j))
            i += 2
            if (i >= N): break
        i0 = ((i0 + 1) % 3)
        j += 1


def bomb8Squares(N,a,b):
    hits=[]
    if ((a-1 >= 0) and (bomb_location(a-1,b))): hits.append((a-1,b))
    if ((a-2 >= 0) and (bomb_location(a-2,b))): hits.append((a-2,b))
    if ((a+1 < N) and (bomb_location(a+1,b))): hits.append((a+1,b))
    if ((a+2 < N) and (bomb_location(a+2,b))): hits.append((a+2,b))
    if ((b-1 >= 0) and (bomb_location(a,b-1))): hits.append((a,b-1))
    if ((b-2 >= 0) and (bomb_location(a,b-2))): hits.append((a,b-2))
    if ((b+1 < N) and (bomb_location(a,b+1))): hits.append((a,b+1))
    if ((b+2 < N) and (bomb_location(a,b+2))): hits.append((a,b+2))
    return(hits)


def find_battleship(N):
    loc=[]
    l1 = getFirstHit(N)
    loc.append(l1)
    (l2,l3) = bomb8Squares(N,l1[0], l1[1])
    loc.append(l2)
    loc.append(l3)
    return(loc)


bLoc = find_battleship(8)
print("\nThe location of the battleship is: ",bLoc,"\n\n")
