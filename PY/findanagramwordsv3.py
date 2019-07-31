#!/usr/local/bin/python3

filename = "/Users/ggerod/WORK/Code/analist01.txt"
file = open(filename, "r")


checkword="glengerod"

for line in file:
   word=(line.strip()).casefold()
   tcw = checkword

   #first remove all the letters in the word from the checkword
   for char in word:
      tcw = tcw.replace(char, "", 1)

   #print("=================")
   #print(word," - ",tcw)

   #then loop through the wordlist to see which ones are contained in the remaining part of checkword
   filename2 = "/Users/ggerod/WORK/Code/analist02.txt"
   file2 = open(filename2, "r")
   for line2 in file2:
      word2=(line2.strip()).casefold()
      tcw2 = tcw

      match=True
      for char in word2:
         if (tcw2.count(char) == 0):
            match=False
            break
         else:
            tcw2 = tcw2.replace(char, "", 1)
      if (match):
         if (len(word2) == len(tcw)):
            print(word, " - ",word2)
   file2.close()
