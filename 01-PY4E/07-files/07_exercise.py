###############################################################
## File Name: 07_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 7 - Files
## Excercise: n/a
## Description: Code walkthrough from lecture and book 
## Other References: associated .txt files in folder
###############################################################

# From Lecture:

# fhand = open('07 - Files/mbox.txt')
# print(fhand)


# xfile = open('07 - Files/mbox.txt')
# count = 0
# for cheese in xfile:    # it is acutally printing each line (not char or string)
#     # print(cheese)
#     count = count + 1
# print("Line Count:", count)


# fhand = open('07 - Files/mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])


# # Search thorugh a file
# fhand = open('07 - Files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip() # remove the duplicate new line by getting rid of the 'whitespace'
#     if line.startswith('From:'):
#         print(line)



# fhand = open('07 - Files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From:"): #Skip lines that you are not interested in
#         continue
#     print(line)     # code that you want to perform on the interested line

# fhand = open('07 - Files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:    # is going to print out all the lines that have that domain in them
#         continue
#     print(line)   

# fname = input('Enter the file name:   ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count = count + 1
# print("There were", count, "Subject lines in", fname)

# EXERCISE 1
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fhand = open('07 - Files/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    print(line.upper())

# EXERCISE 2
# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point
# number on the line. Count these lines and then computer the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        colpos = line.find(":")
        num = line[colpos+1:]
        sum = sum + float(num)
avg = sum/count
print("Average spam confidence: ", avg)


# EXERCISE 3:
# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless easter egg to their program.
# Modify the program that prompts the user for the file name so that it prints a funny message when the user tpes in the exact file name.
# "na na boo boo". The program should behave normally for all other files which exists and don't exist.

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    print("File cannot be opened:", fname)
    exit()
count = 0
sum = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        colpos = line.find(":")
        num = line[colpos+1:]
        sum = sum + float(num)
avg = sum/count
print("Average spam confidence: ", avg)