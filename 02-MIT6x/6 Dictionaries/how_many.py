########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 23, 2022
## Exercise: how many
''' 
Consider the provided sequence of expressions provided below.
We want to write some simple procedures that work on dictionaries to return information.
First, write a procedure, called `how_many`, which returns the sum of the number of values associated with a dictionary.
For example:
>>> print(how_many(animals))
6
'''
########################################################################################################################

# Provided Expressions
animals = { 'a': ['aardvark'], 'b' : ['baboon'], 'c' : ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print(animals)
# {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def how_many(aDict):
    '''
    Write a procedure which returns the sum of the number of values associated with a dictionary
    :param aDict: A dictionary, where all the values are lists
    :return: An integer, the number of values including list items in the dictionary
    '''
    total = 0
    for i in aDict:
        total += len(aDict[i])
    return total

print(how_many(animals))