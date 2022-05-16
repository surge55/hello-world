################################################################################
## File Name: 14_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 14 - Object Oriented Programming 
## Excercise: n/a
## Description: Code walkthrough from book
## Other References: n/a
################################################################################

# Chapter 14 - Object Oriented Programming
class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x=self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('I am destructed', self.x)

# an = PartyAnimal() # construct the object to 'an'

# # tell the object to perform and party() method
# an.party()
# an.party()
# # an.party()

# # self is used to define the scope within each instance that persists within the object

# # print("Type:", type(an))
# # print("Dir:", dir(an))

# an = 42
# print('an contains', an)



# ### Multiple Instances
# class PartyAnimal:
#     x = 0
#     name = ""

#     def __init__(self, z):
#         self.name = z
#         print(self.name, "constructed")
    
#     def party(self):
#         self.x = self.x + 1
#         print(self.name, "party count", self.x)

# s = PartyAnimal("Sally")
# s.party()

# j = PartyAnimal("Jim")
# j.party()
# s.party()



### Inheritance
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))

print(dir(stuff))
