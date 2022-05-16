###############################################################
## File Name: assignment_socket1.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 12 - Network Programming 
## Excercise: Assignment 1 - GRADED
## Description: Retrieve the below url using the HTTP protocol in a way that you 
## can examine the HTTP Response Headers:
## url = 'http://data.pr4e.org/intro-short.txt'
## Enter the headers values in each of the fields below:
## Last-Modifed:
## ETag:
## Content-Length:
## Cache-Control:
## Content-Type:
## Other References: n/a
###############################################################

url = 'http://data.pr4e.org/intro-short.txt'

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0

while True:
    data = mysock.recv(2000)
    if len(data) < 1:
        break
    count += 1
    ddata = data.decode()
    print(ddata)

mysock.close()
