################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge55
## Date: June 16, 2022
## Problem Set 1: 

################################################################################

# GLOBAL Example
s = 'azcbobobegghakl'


################################################################################
# PROBLEM 1
# Assume `s` is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string `s`.
# Valid volwels are a, e, i, o, u.
# For example s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

print('PROBLEM #1:')

# # First Attempt at Solution
# counter = 0
# for chr in s:
#    if chr == 'a':
#        counter += 1
#    if chr == 'e':
#        counter += 1
#    if chr == 'i':
#        counter += 1
#    if chr == 'o':
#        counter += 1
#    if chr == 'u':
#        counter += 1
# print('Number of vowels:', counter)

# More Efficient Version of Problem 1
count = 0 
vowels = 'aeiou'
for char in (s):
   if char in (vowels):
       count += 1
print('Numer of vowels:', count)
  



################################################################################
# PROBLEM 2
# Assume `s` is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in `s`.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

print('PROBLEM #2:')

counter = 0
bob = 0
for char in s:
    if s[counter:counter+3] == 'bob':
        bob += 1
    counter += 1
print('Number of times bob occurs is:', bob)



################################################################################
# PROBLEM 3
# Assume `s` is a string of lower case characters
# Write a program that prints the longest substring of `s` in which the letters occure in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In case of ties, print the frist substring in alphabetical order is: abc

print('PROBLEM #3')

longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Longest substring in alphabetical order is: " + longest)
# Credit given to support from Stackoverflow - Thank You for the Help!