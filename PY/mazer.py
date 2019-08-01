#!/usr/bin/python3


def PrintMat():
    for i in range(8):
        print(MAT[i])
    print()


def MarkAdjacent(i,j):
    #check N
    if ((i > 0) and (MAT[i-1][j] == -1)):
        #mark it and put it on the stack
        MAT[i-1][j] = MAT[i][j] + 1
        stack.append([i-1,j])
    #check E
    if ((j < JRANGE-1) and (MAT[i][j+1] == -1)):
        #mark it and put it on the stack
        MAT[i][j+1] = MAT[i][j] + 1
        stack.append([i,j+1])
    #check S
    if ((i < IRANGE-1) and (MAT[i+1][j] == -1)):
        #mark it and put it on the stack
        MAT[i+1][j] = MAT[i][j] + 1
        stack.append([i+1,j])
    #check W
    if ((j > 0) and (MAT[i][j-1] == -1)):
        #mark it and put it on the stack
        MAT[i][j-1] = MAT[i][j] + 1
        stack.append([i,j-1])
    PrintMat()
    return


IRANGE=8
JRANGE=7
MAT=[[-1 for j in range(JRANGE)] for i in range(IRANGE)]
MAT[7][2] = -2
MAT[7][4] = -2
MAT[4][2] = -2
MAT[4][3] = -2
MAT[4][4] = -2
MAT[1][1] = -2
MAT[1][2] = -2
MAT[1][4] = -2
MAT[1][5] = -2
MAT[7][3] = 0
stack=[[7,3]]

while (stack):
    (i,j) = stack.pop(0)
    MarkAdjacent(i,j)
