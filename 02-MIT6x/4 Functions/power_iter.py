################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: power iter
## Write an iterative function `iterPower(base, exp)` that calculates the
## exponential base^exp by simply using successive multipleicaiton. For example,
## `iterPower(base, exp)` should compute base^exp by multiplying base times itself
## exp times.
##
## This function should take in two values - base can be a float or an integer;
## exp will be an integer >= 0. It should return one numerical value. Your code
## must be iterative - use of the ** operatore is not allowed
################################################################################

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = 1.0
    for x in range(exp):
        ans *= base
    return ans