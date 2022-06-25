########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 23, 2022
## Exercise: biggest
''' 
Consider the provided sequence of expressions provided below.
We want to write some simple procedures that work on dictionaries to return information.
First, write a procedure, called `biggest`, which returns the key corresponding to the entry with the largest number of 
values associated with it. If there is more than one such entry, return any one of the matching keys.
For example:
>>> biggest(animals)
'd'
'''
########################################################################################################################

# Provided expressions
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print(animals)
# {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def biggest(aDict):
    '''
    Write a procedure, which returns the key corresponding to the entry wit ht the lagestnumber of values associated with it.
    If there are more than one such entry, return any one of the matching keys.
    :param aDict: A dictionary, where all the values are lists
    :return: An integer, the number of values including list items in the dictionary
    '''

    myList = []
    currentLen = 0
    
    for i in aDict:
        if len(aDict[i]) >= currentLen:
            myBiggest = i
            currentLen = len(aDict[i])
    return myBiggest

print(biggest(animals))




# Other solution
# print(max(animals))
# print(animals.items())
def otherBiggest(aDict):
    for x,y in aDict.items():
        j=max(aDict)
        return j
# print((otherBiggest(animals)))