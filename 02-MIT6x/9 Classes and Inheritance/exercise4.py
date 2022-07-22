########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 21, 2022
## Exercise: 4
''' 
Python supports a limited form of multiple inheritance, demonstrated in the following code:

'''
########################################################################################################################

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# Assume:
obj = D()

# What happens when these statements are executed
print(obj.a)
'''
D
    C , B
        C (first)
        self.a = 4
'''

print(obj.b)
'''
D
    C, B
        C (none)
        B 
        self.b = 3
'''

print(obj.c)
'''
D
    C, B
        C (frist)
        self.c = 5
'''

print(obj.d)
'''
D
    self.d = 6
'''