#########################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: gcd recur
## The greatest common divisor of two positive integers is the largest integer that divides each of 
## them without remainder. For example,
##
## gcd(2, 12) = 2
## gcd(6, 12) = 6
## gcd(9, 12) = 3
## gcd(17, 12) = 1
##
## A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. 
## Suppose that a and b are two positive integers:
## - If b = 0, then the answer is a
## - Otherwise, gcd(a, b) is the same as gcd(b, a % b)
## Write a function `gcdRecur(a, b)` that implements this idea recursively. This function takes in two 
## positive integers and returns one integer.
##
## Note: In programming there are many ways to solve a problem. For your code to check correctly here, 
## though, you must write your recursive function such that you make a recursive call directly to the 
## function gcdRecur. Thank you for understanding.
#########################################################################################################

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
