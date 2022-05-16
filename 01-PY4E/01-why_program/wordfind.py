###############################################################
## File Name: wordfind.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 1 - Why Would you Learn Programming 
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: http://www.py4e.com/code3/words.py
###############################################################


# 1.8 - What is a program?

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

# You will need to get through Chapter 10 to fully understand 
# the awesome Python techniques that were used to make this program.
