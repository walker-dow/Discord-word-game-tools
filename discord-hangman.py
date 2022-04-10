#! /usr/bin/env python3

import os

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

# Pause if we are running in Windows, to allow users to run the script easily from their file manager or desktop
if os.name == "nt":
    os.system('pause')
