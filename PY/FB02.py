#!/usr/local/bin/python3
import math
# /*
# You will be supplied with two data files in CSV format. The first file
# contains statistics about various dinosaurs. The second file contains
# additional data.
#
# Given the formula:
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#     where g = 9.8 m/s^2 (gravitational constant)
#
# write a program to read in the data files from disk, it must then print the
# names of only the bipedal (i.e. two-legged) dinosaurs from fastest to slowest. Do not print any
# other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
#
#
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal
# */

# dinDict is {NAME: [LEG_LENGTH,DIET,STRIDE_LENGTH,STANCE,SPEED]}
dinDict={}

filename01 = "/Users/ggerod/Desktop/GIT/Code/PY/FBds01.csv"
fh01 = open(filename01, "r")
fh01.readline()  #throw away header line
for line in fh01:
    ddata = line.rstrip().split(',')
    dinDict[ddata[0]] = [float(ddata[1]),ddata[2],None,None]
fh01.close()

filename02 = "/Users/ggerod/Desktop/GIT/Code/PY/FBds02.csv"
fh02 = open(filename02, "r")
fh02.readline()  #throw away header line
for line in fh02:
    ddata = line.rstrip().split(',')
    if (ddata[0] in dinDict.keys()): 
        dinDict[ddata[0]][2] = float(ddata[1])
        dinDict[ddata[0]][3] = ddata[2]
    else: dinDict[ddata[0]] = [None,None,ddata[1],ddata[2]]
fh02.close()

#Compute and add speed
UGC=9.8
for dkey in dinDict.keys():
    if (dinDict[dkey][0] and dinDict[dkey][2]):
        SL = dinDict[dkey][2]
        LL = dinDict[dkey][0]
        speed = ((SL / LL) - 1) * (math.sqrt(LL * UGC))
        dinDict[dkey].append(speed)
    else:
        dinDict[dkey].append(None)

#Finished dictionary
#for dkey in dinDict.keys():
#    print(dkey," : ",dinDict[dkey])

speedDict = {}
for dkey in dinDict.keys():
    if ((dinDict[dkey][3] == 'bipedal') and (dinDict[dkey][4])):
        speedDict[dinDict[dkey][4]] = dkey

speedList = list(speedDict.keys())
speedList.sort(reverse=True)
for element in speedList:
    print(speedDict[element])
