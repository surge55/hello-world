########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 19, 2022
## Exercise: int set
''' 
Consider the code provided below. 
Your task is to define the following two methods for the `inSet` class:
1. Define an `intersect` method that returns a new inSet containing elements that appear in both sets. In other words:
s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. What should happen if s1 and s2 have 
no elements in common.
2. Add the appropriate method(s) so that len(s) returns the number of elements in s.
Hint: Look through the Python Docs to figure out what you'll need to solve this problem
'''
########################################################################################################################

from ssl import OPENSSL_VERSION_INFO


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    # Solution for 1: intersect
    def intersect(self, other):
        """Returns a new intSet (a list) contining elements that appear in both sets (self and other)"""
        newVals = intSet()
        for i in self.vals:
            if i in other.vals:
                # newVals.append(i)
                newVals.insert(i)
        return newVals

    # Solution for 2: len
    def __len__(self):
        count = 0
        for i in self.vals:
            count += 1
        return count


    
# Testing #
# s1 = intSet()
# s1.insert(0)
# s1.insert(1) #
# s1.insert(2) 
# s1.insert(4) #
# s1.insert(7) #
# print(s1)

# s2 = [1,3,4,5,7]

# Test 1: Intersect
# i1 = s1.intersect(s2)
# print(i1)
# print(len(s1))
# print(len(s2))
# print(len(i1))


# t1 = {-19,-18,-8,-7,4,9,10,14,16,19}
# t2 = {-16,-14,-12,-5,-4,8,11,15,19}


# Test Set 1
t1 = intSet()
t1.insert(-19)
t1.insert(-18)
t1.insert(-8)
t1.insert(-7)
t1.insert(4)
t1.insert(9)
t1.insert(10)
t1.insert(14)
t1.insert(16)
t1.insert(19)


# Test Set 2
t2 = intSet()
t2.insert(-16)
t2.insert(-14)
t2.insert(-12)
t2.insert(-5)
t2.insert(-4)
t2.insert(8)
t2.insert(11)
t2.insert(15)
t2.insert(19)

t3 = t1.intersect(t2)

print(t1)
# print(type(t1))
print(t2)
# print(type(t2))
print(t3)