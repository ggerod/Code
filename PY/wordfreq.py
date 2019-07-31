#!/usr/local/bin/python3
import string

filename = "/Users/ggerod/WORK/Code/aesopfables.txt"
file = open(filename, "r")

words = {}
for line in file:
   line=(line.strip()).casefold()
   line = line.translate(line.maketrans('', '', string.punctuation))
   for word in line.split():
      words[word] = words.get(word, 0) + 1

for w in sorted(words, key=words.get, reverse=True):
   print(w,words[w])
