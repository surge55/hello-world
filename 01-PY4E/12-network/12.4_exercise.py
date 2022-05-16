###############################################################
## File Name: 12.4_exercise.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 12 - Network Programming 
## Excercise: 4
## Description: Change the urllinks.py program to extract and count
## paragraph (p) tags from the retrieved HTML document and display 
## the count of the paragraphs as the output of your program. Do not 
## display the paragraph text, only count them. Test you program on
## several small web pages as well as some larger web pages.
## Other References: n/a
###############################################################


from typing import Counter
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
# Count all of the paragrap tags
tags = soup('p')
for tag in tags:
    count += 1

print(count)