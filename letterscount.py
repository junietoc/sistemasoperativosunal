# -*- coding: utf-8 -*-
"""lettersCount.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c8GRyEELh1pCgxirh50HIXho_UdNKsO1
"""

import urllib.request

from string import ascii_lowercase as alphabet

url = "https://qctf.ca/walkthrough/crossword/words.txt"
file = urllib.request.urlopen(url)

wordsFile = open("words.txt","w")
for line in file:
  decoded_line = line.decode("utf-8")
  wordsFile.write(decoded_line)

letterCount = dict((letter,0) for letter in alphabet)

def countLettersWord(word):
  for c in "".join(set(word)):
    letterCount[c] += word.count(c)

words = open("words.txt","r").read()
for w in words.split("\n"):
  countLettersWord(w)

letterCount

