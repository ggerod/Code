#!/usr/bin/python3

alpha="abcdefghijklmnopqrstuvwxyz"
code1="klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"
key="sskkuullll"
i=0
#PT+KY=CT >> PT=CT-KY
for letter in code1:
    #print(letter," - ",alpha.index(letter)," - ",alpha[alpha.index(letter) + 1])
    newindex=(alpha.index(letter) - alpha.index(key[i])) % 26
    i=(i+1)%10
    print(alpha[newindex], end="")

print("=========")
