###############################################################
## File Name: 03_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 1 - Why Would you Learn Programming 
## Excercise: n/a
## Description: Code walkthrough and exercisesfrom book 
## Other References: n/a
###############################################################

# Chapter 3 - Conditional Execution
# Exercises

# Exercise 1: Rewrite your pay computation to give the emoloyee 1.5 times the hourly rate for 
# # hours worked above 40 hours.

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# othours = 0
# otpay = 0

# if hours > 40:
#     othours = hours - 40
#     otpay = othours * rate * 1.5

# totalpay = (hours - othours)*rate + otpay
# print("Pay: ", totalpay)


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program.

# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))

#     if hours > 40:
#         othours = hours - 40
#         otpay = othours * rate * 1.5

#     totalpay = (hours - othours)*rate + otpay
#     print("Pay: ", totalpay)
# except:
#     print("Error, please enter numeric input")



# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of 
# range, print an error mesage. If the score is between 0.0 and 1.0, print a grade using the following table:
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
# < 0.6     F

# try:
#     score = float(input("Enter score: "))

#     if score > 1.0 or score < 0.0:
#         print("Bad Score")
#     elif score >= 0.9:
#         print("A")
#     elif score >= 0.8:
#         print("B")
#     elif score >= 0.7:
#         print("C")
#     elif score >= 0.6:
#         print("D")
#     elif score < 0.6:
#         print("F")
# except: 
#     print("Bad Score")



# Quiz
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)