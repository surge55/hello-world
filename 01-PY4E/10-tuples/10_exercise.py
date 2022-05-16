###############################################################
## File Name: 10_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 10 - Tuples
## Excercise: n/a
## Description: Code walkthrough from lecture & book 
## Other References: n/a
###############################################################


# d = {'a':10, 'b':1, 'c':22}
# t = sorted(d.items())
# print(t)

# for k,v in t:
#     print(k,v)

#     #sorted(d.items()



# Lecture Practice -------------------------------------------------------------------|
# fname = input('Enter File: ')
# if len(fname) < 1 : fname = 'clown.txt'
# hand = open(fname)

# di = dict()
# for lin in hand:
#     lin = lin.rstrip()
#     wds = lin.split()
#     for w in wds:
#         di[w] = di.get(w,0) + 1

# # print(di)

# # Sort this dictionary
# tmp = list()

# for k,v in di.items():
#     new_tuple = (v,k)
#     tmp.append(new_tuple)

# # print('Flipped', tmp)
# tmp = sorted(tmp, reverse=True)
# # print('Sorted', tmp)

# for v,k in tmp[:5]:
#     print(k, v)

# END - Lecture Practice -------------------------------------------------------------------|


# Comparing Tuples -------------------------------------------------------------------------|
# Suppose you have a list of words and you want to sort them from longest to shortest:
# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))
    
# # print(t)
# t.sort(reverse=True)
# # print('sorted:', t)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)
# -----------------------------------------------------------------------------------------|

# Play Ground -----------------------------------------------------------------------------|
# d = {'a':10, 'b':1, 'c':22}

# for key, val in list(d.items()):
#     print(val, key)
# Play Ground - END -----------------------------------------------------------------------|

# Exercise 1 ------------------------------------------------------------------------------|
# Revise a previous program as follows: Read and parse the "From" lines and pull out the
# address from the line. Count the number of messages from each person using a dictionary.
# 
# After all the data has been read, print the person with the most commits by creating a list
# of (count, email) tuples from the dictionary. Then sort the list in reverse order and print
# out the person who has the most commits.

# fname = input("Enter file name: ")
# if len(fname) < 1: fname = "mbox-short.txt"
# fh = open(fname)

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

# vals = list(counts.keys())
# # print(counts)

# lst = list()
# for k, v in counts.items():
#     lst.append((v, k))

# lst.sort(reverse=True)
# for v, k in lst[:1]:
#     print(k, v)
    
# print(lst[0])
# END CODE - Exercise 1 ------------------------------------------------------------------|

# Exercise 2: ----------------------------------------------------------------------------|
# This program counts the distribution of the hour of the dat for each of the messages. You
# can pull the hour from the "From" line by finding the time string and then splitting that 
# into parts using the colon character. Once you have accumulated the counts for each hour,
# print out the counts, one per line, sorted by hour.

fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)

count = 0
counts = dict()

for line in fh:
    line.rstrip()
    if line == "" : continue
    if line.startswith("From"):
        wds = line.split()
        if wds[0] != "From:":
            # print(wds)
            splitd = wds[5].split(":")
            # print(splitd)

            count = count + 1
            counts[splitd[0]] = counts.get(splitd[0], 0) + 1

# vals = list(counts.keys())
# print(counts)

lst = list()
for k, v in counts.items():
    lst.append((k, v))

lst.sort()
for k, v in lst:
    print(k, v)
# --------------------------------------------------------------------------------------|

# Exercise 3 ---------------------------------------------------------------------------|
# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation or anything other than the 
# letters a-z
# 
## NOT COMPLETED NO TIME