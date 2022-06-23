################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: fourth power
## Write a Python function, `fourthPower`, that takes in one number and returns
## that value raised to the fourth power.
##
## You should use the `square` procedure that you defined in an earlier exercise 
## (you don't need to redefine `square` in this box; when you call `square`, the
## grader will use our definition)
## This function takes one number and returns one number.
################################################################################

import square

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(x)**2