################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: eval quadratic
## Write a Python function, `evalQuadratic(a, b, c, x)`, that returns the value
## of the quadratic equation. This function takes one number and returns one number.
################################################################################

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * (x**2) + b * x + c