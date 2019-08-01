#!/usr/bin/python3

leetdict= {
    "a":"@",
    "b":"8",
    "c":"(",
    "e":"3",
    "g":"6",
    "h":"4",
    "i":"!",
    "l":"1",
    "o":"0",
    "s":"$",
    "t":"7",
    "z":"2"
}


def numit(line):
    for i in range(0,10000):
        imod=("%04d" % i)
        print(line + imod)


def capit(line):
    map=[]
    for i in range(0,len(line)):
        if(line[i].isalpha()):
            map.append(i)

    for i in range(0,(2**len(map))):
        perm=bin(i)[2:]
        perm=((len(map)-len(perm))*"0")+perm
        ll=list(line)
        for j in range(0,len(perm)):
            if(perm[j] == '1'):
                ll[map[j]] = ll[map[j]].upper()
        linemod = "".join(ll)
        #print(linemod,end="")
        numit(linemod)


def leetit(line):
    map=[]
    for i in range(0,len(line)):
        if(line[i] in leetdict.keys()):
            map.append(i)

    for i in range(0,(2**len(map))):
        perm=bin(i)[2:]
        perm=((len(map)-len(perm))*"0")+perm
        ll=list(line)
        for j in range(0,len(perm)):
            if(perm[j] == '1'):
                ll[map[j]] = leetdict[ll[map[j]]]
        linemod = "".join(ll)
        #print(linemod,end="")
        capit(linemod)


with open('words.txt', 'r') as f:
    for line in f:
        line=line.rstrip()
        leetit(line.lower())
