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

def find_battleship(N):
    loc=[]
    for i in range(0,N-1):
        for j in range(0,N-1):
          if bomb_location(i,j):
              loc.append((i,j))
              if (len(loc) == 3): return(loc)

bLoc = find_battleship(8)
print("\nThe location of the battleship is: ",bLoc,"\n\n")
