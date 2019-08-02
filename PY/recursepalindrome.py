#!/usr/bin/python3


def ispalindrome(word):
    if (len(word) < 2):
        return(1)
    else:
        if (word[0] != word[(len(word)-1)]):
            return(0)
        else:
            wordnew=word[1:(len(word)-1)]
            print("wordnew = ",wordnew)
            ans=ispalindrome(wordnew)
            return(ans)

WORD="mothraarhtom"
answer=ispalindrome(WORD)
print(WORD,"is a palindrome =",answer)
