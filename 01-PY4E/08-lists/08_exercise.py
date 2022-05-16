###############################################################
## File Name: 08_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 8 - Lists
## Excercise: n/a
## Description: Code walkthrough from lectur and book 
## Other References: associated text files in folder
###############################################################

# FROM LECTURE
# Null

# FROM Textbook

# Exercise 1
# Write a function called chop that takes a list and modifies it, removing the first and last elements
# and returns None. Then write a funciton called middle that tkes a list and returns a new list that
# contains all but the first and last elements

# def chop(t):
#     del t[-1]
#     del t[0]

# def middle(t):
#     return t[1:-1]

# chop_list = ['a', 'b', 'c', 'd']
# mid_list = ['z', 'y', 'x', 'w']

# print('Chopping first and last...')
# print('Current list to chop:', chop_list)
# chop(chop_list)
# print(chop_list)

# print("\nReturning just the middle...")
# print('Current list to middle:', mid_list)
# new_mid = middle(mid_list)
# print('mid_list:', mid_list)
# print('new_mid:', new_mid)

# Exercise 2
# Figure out which line of the above program is still not properly guarded. See if you can construct
# a text file which causes the program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

# Exercise 3
# Rewrite the guardian code in the above example without two if statements. Instead use a compound logical
# expression using the or logical operator with a single if statement


# STRINGS, FILES, LISTS and the GUARDIAN PATTERN

# han = open('mbox-short.txt')

# for line in han:
#     line = line.rstrip()
#     # print('Line:', line)
#     wds = line.split()
#     # print('words', wds)

#     # Guardian pattern
#     # if len(wds) < 3: continue

#     if len(wds) < 3 or wds[0] != 'From': 
#         # print("ignore")
#         continue

#     print(wds[2])


# 8.4 Graded Exercise
# # fname = input('Enter file name: ')
# # fhand = open(fname)

# fhand = open('romeo.txt')
# lst = list()
# for line in fhand:
#     line.rstrip()
#     chk_list = line.split()
#     for i in chk_list:
#         if i in lst: continue
#         lst.append(i)
# lst.sort()
# print(lst)


# 8.5 Graded Exercise
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open("mbox-short.txt")
count = 0

for line in fh:
    line.rstrip()
    if line == "" : continue
    
    if line.startswith("From"):
        wds = line.split()
        
        if wds[0] != "From:":
            count = count + 1
            print(wds[1])
    
print("There were", count, "lines in the file with From as the first word")
