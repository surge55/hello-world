########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 23, 2022
## Exercise: apply to each
''' 
Code for a function `applyToEach` is provided below.
List `testList` is provided below.

Provide an xpression using applyToEach, so that after evaluation testList has the indicated value.
'''
########################################################################################################################

def applyToEach(L, f):
    '''
    Provided by course
    '''
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

## Make Positive
def makePositive(a):
    return abs(a)

testList = [1, -4, 8, -9]   # Reset list
applyToEach(testList, makePositive)
print('Make Positive:')
print(testList)


## Plus One
def plusOne(a):
    return a + 1

testList = [1, -4, 8, -9]   # Reset list
applyToEach(testList, plusOne)
print('Plus One:')
print(testList)


## Square
def square(a):
    return a**2

testList = [1, -4, 8, -9]   # Reset list
applyToEach(testList, square)
print('Square:')
print(testList)