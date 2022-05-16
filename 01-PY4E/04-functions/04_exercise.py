###############################################################
## File Name: 04_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 4 - Functions 
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: n/a
###############################################################

import math
import random

# playground area
# print(math)

# for i in range(10):
#     x = random.randint(5,10)
#     print(x)

# big = max('Hello world')
# print(big)

# tiny = min('Hello world')
# print(tiny)

# Exercise 2/3
# Order of function definitions doesn't matter, but
# a function can't be called until it is defined first 

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# # if call is placed here it will cause an error becuase print_lyric not defined

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# repeat_lyrics()

# Exercise 4
# What is the purpose of the "def" keyword in Python?
# b) it indicates the start of a function
# c) it indicates that the following indented section of code is to be stored for later

# Exercise 5
# What will the following Pythong program print out?
# e) ABC Zap ABC

# def fred():
#     print("Zap")

# def jane():
#     print("ABC")

# jane()
# fred()
# jane()

# Exercise 6
def computepay(hr, rt):
    print("In computepay", hr, rt)
    othours = 0
    otpay = 0
    if hours > 40:
        othours = hr - 40
        otpay = othours * rt * 1.5
    pay = (hr - othours)*rt + otpay
    
    print("Returning pay: ", pay)
    return pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

totalpay = computepay(hours, rate)

print("Pay: ", totalpay)
# print("Error, please enter numeric input")


# # <-------> Answer key from Exercise 3
# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# fh = float(sh)
# fr = float(sr)

# if fh > 4-0:
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh * fr

# print("Pay: ", xp)