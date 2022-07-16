########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 14, 2022
## Exercise: integer division
''' 
Consider the code below and fix the error:

>>>
File "filename.py" line 9, in integerDivision
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
'''
########################################################################################################################

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0 # was missing
    while x >= a:
        count += 1 # operator was backwards
        x = x - a
    return count

# print(integerDivision(5, 3))
print(integerDivision(17, 5))
