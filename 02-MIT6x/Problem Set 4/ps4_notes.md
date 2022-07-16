# Problem Set 4

## wordgame

This game is a lot like Scrabble or Words with Friends. Letters are dealt to players, who then construct one or more words out of their letters. Each **valid** word receives a score, bsed on the length of the word and the letters in that word.



The rules of the game are as follows:

**Dealing**

- A player is dealt a hand of n letters chosen at random (assume n=7)

- The player arranges the hand into as many words as they want out the letters, using each letter at most once.

- Some letters may remain unused (these won't be scored)



**Scoring**

- The score for the hand is the sum of the scores for each word formed

- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plust 50 points if all n letters are used on the first word created.

- Letters are scored as in Scrabble: it is defined in the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

- For example, 'weed' would be worth 32 points (4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)4 = 32. Be sure to check that the hand actually has 1 'w', 2 'e' and 1 'd' before scoring the word.

- As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7 = 105, plus an additional 50 point bonus for using all *n* letters.

Sample Game:

```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```



## Getting Started

1. Download and save Problem Set 4 (files), a zip file of all the skeleton code you'll be filing in. Extract the files from the zip folder and make sure to save all the files in the same folder.

2. Run the file ps4a.py, without making any modifications to it in order to ensure that everything is setup correctly (this means, open the file in IDL, and use the Run command to load the file into the interpreter). The code we have given you loads a list of words from a file and then calls the `playGame` function. You will implement the functions it needs in order to work.

3. The file ps4a.py has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the Helper Code Comments, though you should read and understand how to use each helper function by reading the docstring.

4. This problem set is structured so that you will write a number of modular functions and then glue them together to form the complete word playing game. Instead of waiting unitil the entire game is ready, you should test each function your write, individually, before moving on. This approach is known as unit testing, and it will help you debug your code.



We have provided several test functions to get you started. After you've written each new function, unit test by running the file `test_ps4a.py` to check your work.

If your code passes the unit tests you will see a `SUCCESS` message; otherwise you will see a `FAILURE` message. These tests  aren't exhaustive. You will want to test your code in other ways too.



These are the provided test functions:

`test_getWordScore()` - test the getWordScore() implementation

`test_updateHand()` - test the updateHand() implementation

`test_isValidWord()` - test the isValidWord() implementation





## Problem 1 - Word Score (getWordScore)

The first step is to implement some code that allows us to calculate the score for a single word. The function, `getWordScore` should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.

**Hints:**

- You may assume that the input 'word' is always either a string of lowercase letters or the empty string `""`

- You will want to use the `SCRABBLE_LETTER_VALUES` dictionary defined at the top. You should not change its value.

- Do not assume that there are always 7 letters in a hand! The parameter 'n' is the number of letter required for a bonus score (the maximum number of letters in the hand). Our goal is to keep the code modular - if you want to try playing your word game with n=10 or 4, you will be able to do it by simply changing the value of HAND_SIZE.

- Testing: If this function is implemented properly and you run 'test_ps4a.py', you should see that the 'test_getWordScore()'

tests pass. Also test your implementation of 'getWordScore', using some reasonable English words.



Fill in the code for **getWordScore** in ps4a.py and be sure you've passed the appropraite tests in test_ps4a.py before pasting your function definition for submission.





## Problem #2: Dealing with Hands

The majority of this problem consists of learning how to read code. At the end you will implement a short function.

## Representing Hands

A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following `hand: a, q, l, m, u, i, l.` In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repreated in that hand. For example, the above hand would be represented as:

`hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}`



Notice how the repeated letter 'l' is represented (by a 2). Remember that with a dictionary, the usual way to access a value is hand['a'], where 'a' is the key we want to find. However, this only works if the key is in the dicrionary; otherwise we get a KeyError. For example:

```
>>> hand['e']
Error
>>> hand.get('e', 0)  # returns 0 if no match found in dict
0
```

## Converting words into dictionary representtion

One useful function we've defined for you is **getFrequenctDict**. When givern a string of letters as an input, it returns a dictionary where the keys are letters and the values are number of times that letter is represented in the input string. For example:

```
>>> getFrequency("hello")
{'h':1, 'e':1, 'l':2, 'o':1}
```

As you can see, this is the same kind of dictionary we use to represent hands.

## Displaying a hand

Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have provided the implementation for this in the **displayHand** function. Read through the function and understand what it does and how it works.

## Generating a Random Hand

The hand a player is dealt is a set of letters chosen at random. We provide you with the implementation of a function that generates this random hand, **dealHand**. The function takes as input a positive integer n, and returns a new object, a hand containing n lowercase letters. Again, take a few minues to read through and understand what it does and how it works.

## Removing letters from a hand (you implement this)

The player starts with a hand a set of letters. As the player spells out words, letters from this set are used up.

For example, the player could start out with the following hand `a, q, l, m, u, i, l`. the player could choose to spell the word quail. This would leave the following letters in  the player's hand `l, m`. Your taks is to implement the function **updateHand**, which takes in two inputs - a `hand` and a `word` (string). updateHand uses letters form the hand to spell the word, and then returns a copy of the`hand`, containing only the letters remaining. For example:

```python
>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>>> displayHand(hand) # Implemented for you
a q l l m u i
>>> hand = updateHand(hand, 'quail') # You implement this function!
>>> hand
{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
>>> displayHand(hand)
l m  
```

Implement the updateHand function. Make sure this function has no side effects: ie., it must not mutate the hand passed in. Before pasting your function, be sure you've you've passed the appropriate tests in test_ps4a.py



**Hints**

Testing: Make sure you test updateHand() and updateHand using reasonable inputs.

Copying Dicrionaries: You may wish to use the `.copy` method 

Your implementation of `updateHand` should be short (4 lines of code). It does not need to call any helper functions.





## Problem 3 - Valid Words

At this point, we have written code to generate a random hand (**dealHand**) and display that hand to the user (**displayHand**). We can also ask the user for a word (Python's input) and score the word (using your `getWordScore`). However, at this point we have not written any code to verify that a word given by a plyer obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the `isValidWord` function.

**Testing**: Make sure the test_isValidWord tests pass. In addiion, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behaviour be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for `isValidWord` in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.



## Problem 4 - calculateHandlen

We are now ready to begin writing the code that interacts with the player. We'll be implementing the `playHand` function. This function allows the user to play out a single hand. First, through you'll need to implement the helper `calculateHandlen` function which can be don in under five lines of code.



## Problem 5 - playHand

In ps4a.py, note that the function `playHard`, there is a bunch of pseudocode. The pseudocode is provided to help guide you in writing you function. 

Note: Do not assume that there will always be 7 letters in hand! Ther parameter `n` represents the size of the hand.

Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here are the example output of `playHand`:

#### Case #1

Function Call

```python
wordList = loadWords()
playHand({'h':1, 'i':1, 'c':1 'z':1, 'm':2 'a':1}, wordList, 7)
```

Output:

```python
  Current Hand:  a c i h m m z
  Enter word, or a "." to indicate that you are finished: him
  "him" earned 24 points. Total: 24 points
 
  Current Hand:  a c m z
  Enter word, or a "." to indicate that you are finished: cam
  "cam" earned 21 points. Total: 45 points
 
  Current Hand:  z
  Enter word, or a "." to indicate that you are finished: .
  Goodbye! Total score: 45 points.    
```

#### Case #2

Function Call

```python
wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
```

Output:

```python
  Current Hand:  a s t t w f o
  Enter word, or a "." to indicate that you are finished: tow
  "tow" earned 18 points. Total: 18 points
 
  Current Hand:  a s t f
  Enter word, or a "." to indicate that you are finished: tasf
  Invalid word, please try again.
 
  Current Hand:  a s t f
  Enter word, or a "." to indicate that you are finished: fast
  "fast" earned 28 points. Total: 46 points 
 
  Run out of letters. Total score: 46 points.   
```

#### Case #3

Function Call

```python
wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
```

Output:

```python
  Current Hand: a r e t i i n
  Enter word, or a "." to indicate that you are finished: inertia
  "inertia" earned 99 points. Total: 99 points

  Run out of letters. Total score: 99 points.
```

#### Additional Testing

Test using varying values of `n`. `n` will never be smaller than the number of letters in the hand.



### Function Overview

**`loadWords()`** = returns a list of words that are valid

**`getFrequencyDict(sequence)`** = returns a histogram (dictionary) of the frequency of letters in a word

**`getWordScore(word, n)`** = Returns the score for a word (assumes the word is valid), n is the Hand Size bonus (assumed 7).

**`displayHand(hand)`** = displays the letters currently in the hand (nicer spaced out formatting), from a hand (a dictionary)

**`dealHand(n)`**= returns a random hand of length n as a dictionary

**`updateHand(hand, word)`**= assums hand has all the letters in word. Returns a dicrionary with remaining letters in hand that are not in word

**`isValidWord(word, hand,K wordList)`**= Returns True if word is in word list and is comprised of letters in hand. Otherwise, returns False.

**`calculateHandlen(hand)`**= Returns the length (number of letters in the current hand)

**`playHand(hand, wordList, n)`**= Allows the user to play the given hand

**`playGame(wordList)`**= Allows the user to play an arbitrary number of hands



## Problem 6 - Playing a Game

A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the `playGame` function. You should remove the code that is currently uncommented in the `playGame` body. Read through the specification and make sure you understand what this function accomplishes. For the game you should use the HAND_SIZE constant to determine the number of cards in a hand.



**Testing:** Try out this implementation as if you were playing the game. Try out different values for HAND_SIZE with your program, and be sure that you can play the wordgame iwth different hand sizes by modifying only the vairbale HAND_SIZE.

 

#### Sample Output

```python
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e

```



#### Hints about the output

Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in `playHand` - besure that your code is modular and uses function calls to the `playHard` helper function!

You should also make calls to the `dealHand` helper function. You shouldn't make calls to any other helper function that we've written so far - in fact this function can be written in about 15-20 lines of code.

Here is the above output, with the output from `playHand` obscured:

```python
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e

```

Only submit the function definition for `playGame`

#### A Cool Trick about 'print'

You can make two or more print statements print to the same line! It will spearate the first and second line with a space, and the second and third line with a ? rather than putting each on a new line.





## PART B - Computer

_Part B is dependent on your functions from ps4a.py.__

Now that you have completed your word game code, you decide that you would like to enable your computer (SkyNet) to play the game (your hidden agenda is to prove once and for all that the computers are inverior to human indellect!) In this part, you will be able to compare how you as a user succeed in the game compared to the computer's performance.



You should look at the following two functions: `compChooseWord` and `compPlayHand`.



### compChooseWord

If you follow the pseudocode for compChooseWord, you'll see that th code creates a computer player that is legal, but not always the best. Try to walk through and understand the implementation.

A note on runtime: you may noticie that things run a bit slowly when the computer plays. This is to be expected - the wrodList has 83667 words, after all.

#### Test cases to understand the code

```python
>>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
appels 
>>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
acta 
>>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
immanent 
>>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
None
```

### compPlayHand

Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to Part A's playHand function. This function allows the computer to play a given hand and is very similary to the earlier version in which a user slected the word, although deciding when it is done playing a particular hand idfferens different.



**Test Cases to Understand the Code**

```python
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)

Current Hand: a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.
compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) Current Hand: a a c b t "acta" earned 24 points. Total: 24 points Current Hand: b Total score: 24 points. compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)

Current Hand: a a e e i i m m n n t t
"immanent" earned 96 points. Total: 96 points

Current Hand: a e t i
"ait" earned 9 points. Total: 105 points

Current Hand: e
Total score: 105 points.

```



## Problem 7 - Computer playGame

Now that your computer can choose a word, you need to give the computer the option to pla. Write the code that re-implements the `playGame` function. You will modify the function to bhave as described below in the function's comments. As before, you should use the `HAND_SIZE` constant to determine the number of cards in a hand. Be sure to try out different values for `HAND_SIZE` with your program.



### Here is how the game output should look...

```python
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a s r e t t t
Enter word, or a "." to indicate that you are finished: tatters
"tatters" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a s r e t t t
"stretta" earned 99 points. Total: 99 points

Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: me
Invalid command.

Enter u to have yourself play, c to have the computer play: you
Invalid command.

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a c e d x l n
"axled" earned 65 points. Total: 65 points

Current Hand:  c n
Total score: 65 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a p y h h z o
Enter word, or a "." to indicate that you are finished: zap 
"zap" earned 42 points. Total: 42 points

Current Hand: y h h o
Enter word, or a "." to indicate that you are finished: oy
"oy" earned 10 points. Total: 52 points

Current Hand: h h
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 52 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a p y h h z o
"hypha" earned 80 points. Total: 80 points

Current Hand:  z o
Total score: 80 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```



### Hints about the output

Be sure to inspect the above samle output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in `playHand` and `compPlayHand` - be sure that your code is modular and uses function class to these helper functions!

You should also make the call to the `dealHand` helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

Here is the above output, with the output from `playHand` and `compPlayHand` obscured:

```python
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!
            
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: me
Invalid command.

Enter u to have yourself play, c to have the computer play: you
Invalid command.

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: e

```

### A Note on Runtime

You may notice that thiings run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string->int) so looking up the score of a word becomes much faster in the `compChooseWord` funcion.

Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a world list, for example).

**Important:** Don't worry about this issue when running your code in the checker. We load a very small sample wordList (much smaller than 83667) to avoid having your code timeout. Your code will work even if you don't implement a form of pre-processing as described.



### Entering Your Code

Be sure to only paste your definition for `playGame` from ps4b.py in the submission box. Do not include any other function definitions.
