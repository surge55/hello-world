###############################################################
## File Name: 06_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 6 - Strings
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: n/a
###############################################################

# # From Lecture
# greet = "Hello Bob"
# print(greet)
# greet = greet.lower()
# print(greet)


# Exercise #1
# Write a while loop that starts at the last character in the string 
# and works its way backwards to the fist character in the string, printing
# eacg letter on a separate line, excep backwards.

# my_string = "banana"
# index = len(my_string)-1
# while index >=0 :
#     print(my_string[index])
#     index = index - 1

# Exercise 2
# Given that fruit is a string, what does fruit[:] mean?
# fruit = "banana"
# print(fruit)
# print(fruit[:])

# Exercuse 3
# Encapsulate this code in a function named count, and generalize it
# so taht it accepts the string an the letter as arguments
# def count(word, letter):
#     count = 0
#     for char in word:
#         if char == letter:
#             count = count + 1
#     print("The word", word, "contains", count, letter, "charaters in it.")
# count('banana', 'a')

# Exercise #4 
# There is a string method called count that is similar to the function in the previous exercise. Read the documentation.
# Write an invocation that counts the number of times the letter 'a' occurs in banana.
# fruit = 'banana'
# print(fruit.count('a'))

# Exercise 5
# Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence: 0.8475 '
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a floating point number

colpos = str.find(':')
num = str[colpos+1:]
print(float(num))

# Exercise 6
# Read the string-methods documentation

