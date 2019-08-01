#!/usr/bin/python3


def OutputAlignment(i,j,MAT,row):
    if (i == 0 and j ==0):
        return

    if ((i > 0) and (MAT[i][j] == (MAT[i-1][j] + 1))):
        OutputAlignment(i-1,j,MAT,row)
        if (row == 0):
            print(stringa[i-1],end="")
        else:
            print("-",end="")
    elif ((j > 0) and (MAT[i][j] == (MAT[i][j-1] + 1))):
        OutputAlignment(i,j-1,MAT,row)
        if (row == 0):
            print("-",end="")
        else:
            print(stringb[j-1],end="")
    else:
        OutputAlignment(i-1,j-1,MAT,row)
        if (row == 0):
            print(stringa[i-1],end="")
        else:
            print(stringb[j-1],end="")
        


def EditDistance(A,B):
    DM= [ [ 0 for m in range(len(B)+1) ] for n in range(len(A)+1) ]

    for k in range(len(A)+1):
        DM[k][0] = k
    for k in range(len(B)+1):
        DM[0][k] = k

    for k in range(0,len(A) +1):
        print(DM[k])
    print()

    for j in range(1,len(B)+1):
        for i in range(1,len(A)+1):
            insertion = DM[i][j-1] + 1
            deletion = DM[i-1][j] + 1
            match = DM[i-1][j-1]
            mismatch = DM[i-1][j-1] + 1

            if (A[i-1] == B[j-1]):
                DM[i][j] = min(insertion,deletion,match)
            else:
                DM[i][j] = min(insertion,deletion,mismatch)
    return(DM)


stringa="editing"
stringb="distance"

distmatrix=EditDistance(stringa,stringb)

for i in range(0,len(stringa) +1):
    print(distmatrix[i])
print()

OutputAlignment(len(stringa),len(stringb),distmatrix,0)
print()
OutputAlignment(len(stringa),len(stringb),distmatrix,1)
print()
print()

