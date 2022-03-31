#! /usr/bin/env python3
  
def makeBlanks(word):
    wordBlanks = ""
    for i in word:
        wordBlanks += "\_ "
    return wordBlanks

phrase = input("Please enter phrase for Discord Hangman: ")
phrase = phrase.split()
hangmanPhrase = ""

for word in phrase:
    hangmanPhrase += makeBlanks(word) + "(" + str(len(word)) + ")"
    if word != phrase[len(phrase) - 1]:
        hangmanPhrase += "   "

print(hangmanPhrase)
