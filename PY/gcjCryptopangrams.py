#!/usr/local/bin/python3
import sys

numcases = int(sys.stdin.readline())
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def euc_gcd(a,b):
    while (b!=0):
        t=a
        a=b
        b=t%b
    return(a)


def findfirstnonrepeat():
    for i in range(1,len(cryptedpangram)):
        if (cryptedpangram[i] != cryptedpangram[i-1]):
            return(i)


def unzipbackward(goodindex):
    for i in range(goodindex,0,-1):
        # look at 2 prime factors
        # see if the first is in the previous composites set
        if (factorlist[i][0] not in factorlist[i-1]):
            # swtich the order of factorlist[i]
            factorlist[i].reverse()
        # now see if you need to fix factorlist[i-1]
        if (factorlist[i-1][1] != factorlist[i][0]):
            # swtich the order of factorlist[i-1]
            factorlist[i-1].reverse()


def unzipforward(goodindex):
    for i in range(goodindex+1,len(factorlist)):
        if (factorlist[i][0] != factorlist[i-1][1]):
            factorlist[i].reverse()


def makefactorlist(complist):
    Factored={}
    factorlist=[]
    for i in range(len(complist)-1):
        gcdofprimes = euc_gcd(complist[i],complist[i+1])
        n1otherprime = int(complist[i]/gcdofprimes)
        n2otherprime = int(complist[i+1]/gcdofprimes)
        n1list = [gcdofprimes,n1otherprime]
        n2list = [gcdofprimes,n2otherprime]
        if (1 not in n1list):
            Factored[complist[i]] = n1list
        if (1 not in n2list):
            Factored[complist[i+1]] = n2list
    for compnum in complist:
        factorlist.append(Factored[compnum])
    return(factorlist)


for casenum in range(numcases):
    print("Case #"+str(casenum+1)+": ",end="")
    (maxprimesize,listlength) = ((sys.stdin.readline()).rstrip()).split()
    cryptedpangramin = (sys.stdin.readline()).rstrip()
    cryptedpangram = [int(x) for x in cryptedpangramin.split()]
    factorlist=[]
    primeseq=[]

    factorlist = makefactorlist(cryptedpangram)

    # find the first non repeating composite number in the composite sequence
    firstgoodindex = findfirstnonrepeat()

    # unzip factorlist backwards from the first nonrepeating index point
    unzipbackward(firstgoodindex)

    # proceed arranging factorlist forward from the first nonrepeating index point
    unzipforward(firstgoodindex)

    # create the ordered list of primes which map to the alphabet
    for i in range(len(factorlist)):
        primeseq.append(int(factorlist[i][0]))
    primeseq.append(int(factorlist[len(factorlist)-1][1]))
    pseqordereduniq = (primeseq.copy())
    pseqordereduniq = list(set(pseqordereduniq))
    pseqordereduniq.sort()

    # Now decode the message
    for prime in primeseq:
        print(alphabet[(pseqordereduniq.index(prime))],end="")
    print()
