###############################################################
## File Name: 09_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 9 - Dictionaries
## Excercise: n/a
## Description: Code walkthrough from lecture & book 
## Other References: .txt files in folder
###############################################################


# FROM LECTURE
# Counting Pattern
# counts = dict()
# print("Enter a line of text:")
# line = input("")

# words = line.split()

# print("Words:", words)

# print("Counting...")
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Counts:', counts)


# Count all the words in the file
# name = input("Enter file:")
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)


# Exercise 1 --------------------------------------------------------------------------------------- |
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary

# name = 'words.txt' # input("Enter file:")
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0)

# if 'tasks' in counts:
#     print("the word is there")

# ------------------------------------------------------------------------------------------------- |

# counts = {'chuck':1, 'annie':42, 'jan':100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# counts = {'chuck':1, 'annie':42, 'jan':100}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(key, counts[key])
# print(lst)

# Exercise 2 -------------------------------------------------------------------------------------- |
# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a 
# running count of each of the days of the week. At the end of the program print out the contents
# of your dictionary (order does not matter).

# fname = "mbox-short.txt"
# fh = open("mbox-short.txt")
# count = 0
# counts = dict()

# for line in fh:
#     line.rstrip()
#     if line == "" : continue
    
#     if line.startswith("From"):
#         wds = line.split()
        
#         if wds[0] != "From:":
#             count = count + 1
#             counts[wds[2]] = counts.get(wds[2], 0) + 1
#             # print(wds[2])
# print(counts)
# ------------------------------------------------------------------------------------------------ |

# Exercise 3 ------------------------------------------------------------------------------------- |
# Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.

# ANSWER same as exercise 2, you just change wds[2] to wds[1]

# fname = "mbox-short.txt"
# fh = open("mbox-short.txt")
# count = 0
# counts = dict()

# for line in fh:
#     line.rstrip()
#     if line == "" : continue
    
#     if line.startswith("From"):
#         wds = line.split()
        
#         if wds[0] != "From:":
#             count = count + 1
#             counts[wds[1]] = counts.get(wds[1], 0) + 1
#             # print(wds[2])
# print(counts)
# ----------------------------------------------------------------------------------------------- |

# Exercise 4 ------------------------------------------------------------------------------------ |
# Add code to the above program to figure out who has the most messages in the file. After all
# the data has been read and the dictionary has been created, look through the dictionary using a
# maximum loop to find who has the most messages and print how many messages the person has

fname = "mbox-short.txt"
fh = open("mbox.txt")
count = 0
counts = dict()

for line in fh:
    line.rstrip()
    if line == "" : continue
    if line.startswith("From"):
        wds = line.split()
        if wds[0] != "From:":
            count = count + 1

            counts[wds[1]] = counts.get(wds[1], 0) + 1

vals = list(counts.keys())
largestsofar = 0
for key in counts:
    if counts[key] > largestsofar:
        largestsofar = counts[key]
        name = key
print(name, largestsofar)
# ----------------------------------------------------------------------------------------------- |
# ANSWER KEY
# fname = input('Enter File: ')
# if len(fname) < 1 : fname = 'clown.txt'
# hand = open(fname)

# di = dict()
# for lin in hand:
#     lin = lin.rstrip()
#     wds = lin.split()
#     for w in wds:
#         di[w] = di.get(w,0) + 1

# largest = -1
# theword = None
# for k,v in di.items():
#     if v > largest:
#         largest = v
#         theword = k

# print(theword, largest)
# Answer END -------------------------------------------------------------------|




# Exercise 5 ------------------------------------------------------------------------------------ |
# This program records the domain name (instead of the address) where the message was sent from
# instead of who the email came from (ie the whole email address). At the end of the program, 
# print out the contents of your dictionary

# fname = "mbox-.txt"
# fshort = "mbox-short.txt"
# fh = open(fshort)
# count = 0
# counts = dict()

# for line in fh:
#     line.rstrip()
#     if line == "" : continue
#     if line.startswith("From"):
#         wds = line.split()
#         if wds[0] != "From:":
#             count = count + 1
#             dom = wds[1].split('@')
#             counts[dom[1]] = counts.get(dom[1], 0) + 1

# print(counts)
# ----------------------------------------------------------------------------------------------- |