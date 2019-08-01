#!/usr/bin/python3

alpha="abcdefghijklmnopqrstuvwxyz"
#code1="themagicwordsaresqueamishossifrage"
code1="nlupbzdpaovbalkbjhapvupzsprlzpsclypuaoltpul"

for i in range(0,27):
    print(i,">>")
    for letter in code1:
        #print(letter," - ",alpha.index(letter)," - ",alpha[alpha.index(letter) + 1])
        newindex=(alpha.index(letter) + i) % 26
        #print("newindex=",newindex)
        print(alpha[newindex], end="")
    print("---")
