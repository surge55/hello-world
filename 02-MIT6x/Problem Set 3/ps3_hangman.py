########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 23, 2022
## Problem Set 3: hangman
''' 
For this problem, you wil implement a variation of the classic word game Hangman. In this problem, the second player 
will always be the computer, who will be picking a word at random.

Please see the ps3_notes.md file for full details.
'''
########################################################################################################################


# Hangman game
# ----------------------------------------------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from glob import glob
from operator import truediv
import random
import string
from webbrowser import get

# Global Variables
lb = "-------------"
guessesLeft = 8
WORDLIST_FILENAME = "/Users/surge/code_repo/hello-world/02-MIT6x/Problem Set 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()     # splits the string into a List, you can specify the separator (default is white space)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# ----------------------------------------------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# PROBLEM #1
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    score = 0
    # while score != len(secretWord):
    for i in lettersGuessed:
        # print(i)
        if i in secretWord:
            # print(i)
            score += 1
            # print(score, "\n")
    if score >= len(secretWord):
        return True
    else:
        return False

# Test isWordGuessed
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# # lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a','l', 'l']
# print(isWordGuessed(secretWord, lettersGuessed))


# PROBLEM #2
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    gString = ""
    for i in secretWord:
        if i in lettersGuessed:
            gString += i #+ " "
        else:
            gString += "_ "
    return gString

# Test getGuessedWord
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# PROBLEM 3
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # abet = string.ascii_lowercase
    rChar = ""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            rChar += i
    return rChar

# Test getAvailableLetters
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))


# PROBLEM 4
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # global guessesLeft
    guessesLeft = 8
    lb = "-------------"

    # Intro to Game
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is", len(secretWord), "letters long.")

    # Guessing Play
    while "_" in getGuessedWord(secretWord, lettersGuessed) or guessesLeft > 0:
        if getGuessedWord(secretWord, lettersGuessed).strip() == secretWord or guessesLeft <= 0:
            break

        print(lb) ## line break
        print("You have", guessesLeft, "guesses left")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        newGuess = input("Please guess a letter: ")
        if newGuess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(newGuess)
            if newGuess in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
        
    
    # Final Game Result    
    final = getGuessedWord(secretWord, lettersGuessed).strip()
    print(lb) # line break
    if final == secretWord:
        print('Congratulations, you won!') ## you win
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = "else"
hangman(secretWord)
