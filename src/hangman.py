'''
Hangman game with one or two players for the console.
Author: Matthias Sieber <empower@manonthemat.com>
'''

import os # for clear/cls function to clear the screen
from sys import platform as _platform # to find out the actual OS to either use cls or clear
import random # for random choice of a word in one player mode

theWord = '' # this is the word that has to be guessed - use globally in functions
partialWord = '' # this is the word with the guessed letters in place and underscores where there's still letters to guess 
fails = 0 # number of wrong guesses
HANGMAN = ("""

  +---+
  |   |
  |   |
      |
      |
      |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
      |
      |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
  |   |
      |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
 /|   |
      |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
 /|\  |
      |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
 /|\  |
 /    |
      |
      |
=========
      
""","""

  +---+
  |   |
  |   |
  o   |
 /|\  |
 / \  |
      |
      |
=========
      
""")
def chosePlayer(player):
    if player == "1":
        print ("I, the computer will think of a word for you to guess.")
        setTheWord(getAWord())
        input ("Ok, I'm ready. Hit enter to start guessing.")
    elif player == "2":
        print ("Okay. Player 1, you think of a word and type it in.")
        print ("Make sure Player 2 doesn't see it!")
        setTheWord(input ("The word shall be: "))
    else:
        print ("You don't want to play? That's alright with me!\a\nEOG")
        exit() # just get out of here

def getAWord():
    file = open("hangdic.txt","r")
    word = random.choice(list(file)) # from http://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
    return word[:-1] # we don't want the trailing line-break in the word, thus -1

def setTheWord(word):
    global theWord # need to modify the word globally... there can only be one word
    global partialWord
    theWord = word.lower()
    lengthOfTheWord = len(theWord)
    i = 0
    while i != lengthOfTheWord:
        partialWord += "_"
        i += 1

def clearScreen():
    if _platform == "cygwin32" or _platform == "win32" or _platform == "win" or _platform == "win64":
        os.system("cls") # for windows
    else:
        os.system("clear") # for everything else - like Mac/Unix

def showHangman(a):
    global fails
    fails = a
    print (HANGMAN[fails])

def showWord():
    global partialWord
    print (partialWord)

def guessALetter():
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        print ("Be advised: Enter a single letter!\n\a(Hit enter to try again)")
        input()
    else:
        guess = guess.lower()
        checkLetterInWord(guess)

def checkLetterInWord(letter):
    global theWord
    global partialWord
    global fails
    if (letter in theWord) == False:
        fails += 1
    else:
        i = 0
        while i < len(theWord):
            x = theWord.find(letter, i) # find the position of the letter in theWord
            if x != -1:
                partialWord = partialWord[:x] + letter + partialWord[x+1:]
            i+=1
            

def main():
    clearScreen()
    chosePlayer(input("How many players? (1 or 2): "))
    while fails < 6:
        clearScreen()
        showHangman(fails)
        showWord()
        guessALetter()
        if partialWord == theWord:
            clearScreen()
            showHangman(fails)
            showWord()
            print ("You got it!\n\aVictory is yours!")
            exit(0) #exit the program, you won!
    clearScreen()
    showHangman(fails)
    print ("\aYou lose - You hang!") # since you didn't win, you lose and hang!
    print ("The word was",theWord)

if __name__ == "__main__":
    main()
