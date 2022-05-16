###############################################################
## File Name: 05_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 5 - Loops and Iteration 
## Excercise: n/a
## Description: Code walkthrough and exercise from lecure and book 
## Other References: n/a
###############################################################

# FROM Lecture

# part one
# n = 5
# while n > 0:
#     print(n)
#     n = n -1
# print('BLASTOFF!')
# print(n)

# part two
# friends = ['Joseph', 'Glenn', 'Sally']
# for i in friends:
#     print('Happy New Year:', i)
# print("Done")

# part three
# What is the largest number?

# from typing import Counter


# largest_so_far = -1
# num_list = [9, 41, 12, 3, 74, 15]

# print("Before", largest_so_far)
# for i in num_list:
#     if i > largest_so_far:
#         largest_so_far = i
#     print(largest_so_far, i)

# print('After', largest_so_far)



# Exercises 5.9 -----------_>


# Exercise 1
# Write a program which repeatedly reads numbers until the user enters "done".
# Once 'done' is entered, print out the total, count and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number

# count = 0
# total = 0
# average = 0
# # try:
# while True:
#     ent_num = input("Enter a number: ")
#     if ent_num == "done":
#         print(total, count, average)
#         break
#     try:
#         int_num = int(ent_num)
#         count = count + 1
#         total = total + int_num
#         average = total / count
#     except:
#         print("Invalid Input")


# Exercise 2
# Write another program that prompts for a list of numbers as above and at the end 
# prints out both the maxium and minimum of the numbers instead of the average

count = 0
total = 0
average = 0
smallest = None
largest = None

# try:
while True:
    ent_num = input("Enter a number: ")
    if ent_num == "done":
        print(total, count, smallest, largest)
        break
    try:
        int_num = int(ent_num)
        count = count + 1
        total = total + int_num
        average = total / count

        # calculate min value
        if smallest is None or int_num < smallest:
            smallest = int_num

        # calculate max value
        if largest is None or int_num > largest:
            largest = int_num

    except:
        print("Invalid Input")


# Exercise 5.2 AUTOGRADER
# 10/10
count = 0
total = 0
average = 0
smallest = None
largest = None

# try:
while True:
    ent_num = input("Enter a number: ")
    if ent_num == "done":
        # print(total, count, smallest, largest)
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        int_num = int(ent_num)
        count = count + 1
        total = total + int_num
        average = total / count

        # calculate min value
        if smallest is None or int_num < smallest:
            smallest = int_num

        # calculate max value
        if largest is None or int_num > largest:
            largest = int_num

    except:
        print("Invalid input")