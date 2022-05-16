###############################################################
## File Name: 11_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 11 - Regular Expressions
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: associated files in folder
###############################################################


#11.2 Extracting data using regular expressions

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print(lst)  

# We can use this regular expression in a program
# to read all the lines in a file and print out
# anything that looks like an email address:
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)

## Much Cleaner Version
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)

# Search for lines that start with "X" followed by any
# non-whitespace characters and ':'
# followed by a space and any number
# the number can include a decimal
# import re
# hand = open('mbox-short.txt')

# # Returns a List
# # for line in hand:
# #     line = line.rstrip()
# #     x = re.findall('^X\S*: [0-9.]+', line)
# #     if len(x) > 0:
# #         print(x)
# #         print(type(line))

# # Returnes a String
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X\S*: [0-9.]+', line):
#         print(line)
#         # print(type(line))



# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal
# Then print the number if it is greater than 0

# import re
# hand = open('mbox-short.txt')

# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)


# Exercise 1
# Write a simple program to simulate the operation of the grep
# command on unix. Ask the user to enter a regular expression 
# and count the nuber of lines that matched the regular expression:

# import re

# reg_inp = input("Enter a regular expression: ")
# count = 0

# hand = open('mbox.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search(reg_inp, line):
#         count += 1

# print('mbox.txt had', count, 'lines that match', reg_inp)



# Exercise 2
# Write a program to look for lines of the form:
# 'New Revision: 39772'
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers
# and print out the average as an integer.

# import re
# hand = open('mbox.txt')
# total = 0
# count = 0

# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^New Revision: ([0-9]+)', line)
#     if len(x) > 0:
#         for i in x:
#             total = total + float(i)
#             count += 1

# print(int(total/count))


# FINDING NUMBERS IN A HAYSTACK
# In this assignment you will read through and parse a file with text and numbers
# You will extract all the numbers in the file and compute the sum
# of  the numbers 

import re
hand = open('regex_sum_act.txt')
total = 0
count = 0

for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        # print(x)
        for i in x:
            total += float(i)

print('sum is', int(total))
