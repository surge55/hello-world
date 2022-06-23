################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: odd
## Write a Python function, `odd`, that takes in one number and returns True 
## when the number is odd and False otherwise.
##
## You should use the % (mod) operatore, not `if`
## 
## This function takes one number and returns one number.
################################################################################

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    if x % 2 == 0:
        return False
    else:
        return True