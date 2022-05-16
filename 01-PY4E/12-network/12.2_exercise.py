###############################################################
## File Name: 12.2_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 12 - Network Programming 
## Excercise: 2
## Description: Change your socket program so that it counts the number
## of characters it has received and stops displaying any text after 
## it has shown 3000 characters. The program should retrieve the entire
## document and count the total number of characters and display the 
## count of the number of characters at the end of the document. 
## Other References: n/a
###############################################################


import urllib.request, urllib.parse, urllib.error

# Prompt User to enter URL
# URL = input("Enter the URL: ")
URL = 'http://data.pr4e.org/romeo.txt'

# Check if URL is valid
ls_URL = URL.split('/')
if ls_URL[0] != "http:" and ls_URL[0] != "https:":
    print("Please try again using HTTP://... Format")

# Open URL as file Handler
fhand = urllib.request.urlopen(URL).read().decode()
# d_fhand = fhand.decode()
count = 0

for char in fhand:
    if count <= 3000:
        print(char, end='')
    count += 1
print('Total:', count)