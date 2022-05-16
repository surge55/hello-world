###############################################################
## File Name: 12_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 12 - Network Programming
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: n/a
###############################################################


# Building a Web Browser in Python
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512) # receive up to 512 characters
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# EXAMPLE: Sockets - Simpler version using urllib
# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('https://thinqapp.com')
# for line in fhand:
#     print(line.decode().strip())

# EXAMPLE: Using URLLIB & BeautifulSoup Library
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input("Enter - ")
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, "html.parser")

# # retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href',None))


## Retrieving an Image of HTTP
# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#     data = mysock.recv(5120)
#     if len(data) < 1: break
#     time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data

# mysock.close()

# # Look for the end of the header (2 CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header length', pos)
# print("PRINTING HEADER...")
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# print("saving picture...")
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()
# print('DONE')


# Breakup the HTTP request for Large FILES
# from typing import Sized
# import urllib.request, urllib.parse, urllib.error

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
# fhand = open('cover3.jpg', 'wb')
# size = 0
# while True:
#     info = img.read(100000)
#     if len(info) < 1: break
#     size = size + len(info)
#     fhand.write(info)

# print(size, "characters copied.")
# fhand.close()


# EXERISE 1
# Change the socket1.py to prompt the user for the URL so it can read any web page
# you can use split('/') to break the url into its component parts so you can
# extract the host name for the socket connect call. Add error checking
# using try and except to handle the condition where the user enters an
# improperly formatted or non-existent URL.

# import socket

# URL = input("Enter the URL: ")

# try:
#     ls_URL = URL.split('/')
#     # print(ls_URL[0])
#     if ls_URL[0] != "http:" and ls_URL[0] != "https:":
#         print("Please try again using HTTP://... Format")
        
#     # print(ls_URL)

#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # print(ls_URL[2])
#     mysock.connect((ls_URL[2], 80))
#     cmd = 'GET '+ URL + ' HTTP/1.0\r\n\r\n'
#     # print("cmd: ", cmd)
#     mysock.send(cmd.encode())

#     while True:
#         data = mysock.recv(512)
#         if len(data) < 1:
#             break
#         print(data.decode(),end='')

#     mysock.close()
# except:
#     print("Please try again using HTTP://... Format")
# http://data.pr4e.org/romeo.txt



# EXERCIES 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after 
# it has shown 3000 characters. The program should retrieve the entire
# document and count the total number of characters and display the 
# count of the number of characters at the end of the document.

import socket

URL = input("Enter the URL: ")

# try:
ls_URL = URL.split('/')
# print(ls_URL[0])
if ls_URL[0] != "http:" and ls_URL[0] != "https:":
    print("Please try again using HTTP://... Format")
    
# print(ls_URL)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(ls_URL[2])
mysock.connect((ls_URL[2], 80))
cmd = 'GET '+ URL + ' HTTP/1.0\r\n\r\n'
# print("cmd: ", cmd)
mysock.send(cmd.encode())
count =  0


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    excerpt = data.decode().read(3000)
    print(excerpt)
    count += 1
    print('Count:', count)

mysock.close()
print("Total: ", count)
# except:
    # print("Please try again using HTTP://... Format")
# http://data.pr4e.org/romeo.txt



import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())