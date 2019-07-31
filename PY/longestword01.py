#!/usr/local/bin/python3

filename = "/usr/share/dict/words"
file = open(filename, "r")

longestword=''
longestwordlen=0
for line in file:
   word=(line.strip()).casefold()
   if (len(word) <= longestwordlen):
      continue

   norepeat = True
   for char in word:
      if (word.count(char) > 1):
         norepeat=False
         continue
   
   if (norepeat):
      longestword=word
      longestwordlen = len(word)
      print("new longest word =",word)

print("The longest word with no repeated letters in ",filename, " is: ",longestword)
