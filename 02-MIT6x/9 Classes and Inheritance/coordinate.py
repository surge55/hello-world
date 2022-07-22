########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 19, 2022
## Exercise: coordinate
''' 
Consider the code provided below. Your task is to define the following two methods for the Coordinate class:
1. Add an `__eq__` method that returns True if coordinates refer to the same point in the plane (e.g. have the same x and y)
2. Define `__repr__`, a special method that returns a string that looks like a valid Python expression that could be used
to recreate an object with the same value. In other words, eval(repr(c)) == c, given the definition of __eq__ from part 1.
'''
########################################################################################################################

from re import X


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # Returns True if self and other have the same coordinates
        return (self.x == other.x) and (self.y == other.y)
    
    def __repr__(self):
        return "Coordinate(%d,%d)" % (self.x, self.y)

# Testing
x = Coordinate(3,4)
print(x)
print(repr(x))