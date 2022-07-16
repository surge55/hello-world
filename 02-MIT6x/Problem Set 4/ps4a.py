########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 14, 2022
## Problem Set 4: The 6.00 Word Game
''' 
See ps4_notes.md for full details of Problem Set 4.
'''
########################################################################################################################

from cgi import test
import random
import string
from turtle import update

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------






########################################################################################################################
## Problem 1 - Word Score (getWordScore)
'''
The first step is to implement some code that allows us to calculate the score for a single word. The function, 
`getWordScore` should accept as input a string of lowercase letters (a word) and return the integer score for that word,
using the game's scoring rules.

Fill in the code for getWordScore in ps4a.py and be sure you've passed the appropraite tests in test_ps4a.py before pasting
your function definition for submission.
'''
########################################################################################################################

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    # Score points per letter times word length
    score = 0
    for ch in word:
        score += SCRABBLE_LETTER_VALUES[ch]
    score *= len(word)

    # Check if Bonus Points (50)
    if len(word) >= n:
        score += 50
    
    return score

# For testing
# long_word = 'triplet'
# print(getWordScore(long_word, 8))








########################################################################################################################
## Problem #2: Dealing with Hands
'''
The majority of this problem consists of learning how to read code. At the end you will implement a short function.

See ps4_notes.md for full details of Problem 2.
Implement the updateHand function.

'''
########################################################################################################################

# displayHand is provided
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

# dealHand is provided
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


# Problem #2: Update a hand by removing letters
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for ch in word:
        ch_count = newHand.get(ch, 0)
        if ch_count > 0:
            if ch_count == 1:
                newHand.pop(ch)
            else:
                newHand[ch] = ch_count - 1
    return newHand
# test updateHand()
# testHand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i':1}
# word = "quail"
# print(updateHand(testHand, word))





########################################################################################################################
## Problem #3: Valid Words
'''
A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the 
`isValidWord` function.

Fill in the code for `isValidWord` in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before 
pasting your function definition here.

Tests:
- Call multiple times on the same hand - what should happen?
- "" an empty string
'''
########################################################################################################################

# Problem #3: Test word validity
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # check blank string
    if word == "":
        # print("word is blank")
        return False
    
    temp_hand = hand.copy()
    # check that word is in hand
    for ch in word:
        if temp_hand.get(ch, 0) == 0:
            # print("letter is not in hand")
            return False
        elif temp_hand.get(ch, 0) > 0:
            temp_hand[ch] = temp_hand.get(ch, 0) - 1
    
    # check that word is in wordList
    if word in wordList:
        # print("word is in word list")
        return True
    else:
        return False

# Testing
# my_word = "rapture"
# my_hand = {'a': 3, 'r': 1, 'u': 1, 'e': 1, 't': 1, 'p': 2}
# all_words = loadWords()
# print(isValidWord(my_word, my_hand, all_words))






########################################################################################################################
## Problem #4: Playing a hand
'''
We are now ready to begin writing the code that interacts with the player. We'll be implementing the `playHand` function. 
This function allows the user to play out a single hand. First, through you'll need to implement the helper 
`calculateHandlen` function which can be don in under five lines of code.
'''
########################################################################################################################

# Problem #4: Playing a hand
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    num_letter = 0
    for letter in hand:
        num_letter += hand[letter]
    return num_letter

# Testing
# my_hand = {'a': 3, 'r': 1, 'u': 1, 'e': 1, 't': 1, 'p': 2}
# print(calculateHandlen(my_hand))






########################################################################################################################
## Problem #5: playHand
'''
In ps4a.py, note that the function `playHard`, there is a bunch of pseudocode. The pseudocode is provided to help guide 
you in writing you function.
Note: Do not assume that there will always be 7 letters in hand! Ther parameter `n` represents the size of the hand.
Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. 
Here are the example output of `playHand
'''
########################################################################################################################

# Problem #5: playHand
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    totalPoints = 0

    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current Hand:", end=" ")
        displayHand(hand)
        
        user_play = input('Enter word, or a "." to indicate that you are finished: ')
        if user_play == '.':
            print('Goodbye! Total score: ' + str(totalPoints) + ' points.')
            break
        else:
            if not isValidWord(user_play, hand, wordList):
                print("Invalid word, please try again")
                print() # new line
            else:
                pointsEarned = getWordScore(user_play, n)
                totalPoints = totalPoints + pointsEarned
                print('"' + user_play + '" earned ' + str(pointsEarned) + ' points. Total: ' + str(totalPoints) + ' points')
                print() # new line
                hand = updateHand(hand, user_play)
    
    if calculateHandlen(hand) == 0:
        print("Run out of letters. Total score: " + str(totalPoints) + " points.")


# Testing
# wordList = loadWords()
# playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
# playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
# playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)








########################################################################################################################
## Problem #6: Playing a game
'''
In ps4a.py, note that the function `playHard`, there is a bunch of pseudocode. The pseudocode is provided to help guide 
you in writing you function.
Note: Do not assume that there will always be 7 letters in hand! Ther parameter `n` represents the size of the hand.
Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. 
Here are the example output of `playHand
'''
########################################################################################################################

# Problem #6: Playing a game
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """

    play_game = ""


    while play_game != 'e':
        play_game = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # Deal New Hand
        if play_game == 'n':
            lastHand = dealHand(HAND_SIZE)
            playHand(lastHand, wordList, HAND_SIZE) # I thought you should put a fixed constant for Bonus size of 7 which may be different than HAND_SIZE
        
        # Replay Last Hand
        elif play_game == 'r':
            try:
                lastHand
            except:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(lastHand, wordList, HAND_SIZE)
        
        # End Game
        elif play_game =='e':
            break
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
