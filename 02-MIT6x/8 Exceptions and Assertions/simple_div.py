########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 14, 2022
## Exercise: simple divide
''' 
Suppose we rewrite the fancy_divide function to user a helper function
Change the definition of simple_divide so that the call does not raise an exception.
When dividing by 0, fancy_divide should return a list with all 0 elements.
Any other error case should still raise exceptions.
You should only handle the ZeroDivisionError.
'''
########################################################################################################################

from decimal import DivisionByZero


def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    
    except ZeroDivisionError:
        return 0

print(fancy_divide([0, 2, 4], 0))
print(fancy_divide([0, 2, 4], 1))
