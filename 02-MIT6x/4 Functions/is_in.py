#########################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: is in
''''
We can use the idea of bisection search to determine if a character is in a string, so long as the string 
is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need 
only consider the lower half of the string; otherwise, we only consider the upper half of the string. 
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in 
aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function 
should return a boolean value.

As you design the function, think very carefully about what the base cases should be.

Note: In programming there are many ways to solve a problem. For your code to check correctly here, though, 
you must write your recursive function such that you make a recursive call directly to the function isIn. 
Thank you for understanding.

BASIC FUNCTION STRUCTURING
Be very careful about how you slice the string in the recursive cases! Before you execute the recursive cases, 
you test the middle character - so if you reach the recursive cases, you know the middle character cannot be 
a match, right? So be careful to not include this character when you make your recursive call!

WHAT SHOULD YOUR BASE CASE BE?
You should be thinking about 3 situations:
- What happens when the string is empty?
- What happens when the string is of length 1?
- What happens when the test character equals the middle character?

WHAT SHOULD YOUR RECURSIVE CASE BE?
- What happens when the test character is smaller than the middle character?
- What happens when it is larger?
'''
#########################################################################################################

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Base case: If aStr is empty return false
    if aStr == '':
        return False

    # Base case: If aStr is of length 1, compare if characters are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: If the middle character of aStr equals the character
    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    if char == midChar:
        return True

    # Recursive: If the test char is smaller than the middle char, recursively search on  first half of string
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    #  Test char is larger than the middle char, recursively search on the second half of string
    else:
        return isIn(char, aStr[midIndex + 1:])