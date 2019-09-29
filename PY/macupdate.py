#!/usr/local/bin/python3

#with open('gdg.csv', 'r') as myfile:
with open('zzz', 'r') as myfile:
    #myfile.readline() #throw away the first line
    for line in myfile:
        #macin = (line.split(',')[0]).split('"')[1]
        #macin = line.split('"')[1]
        macin = line.rstrip()
        macin = macin.replace(":","")
        cpe_mac = (hex(int(macin, base=16) - 2))[2:]
        if (len(cpe_mac) != 12):
           cpe_mac = ('0'*(12 - len(cpe_mac))) + cpe_mac
        print(cpe_mac)
