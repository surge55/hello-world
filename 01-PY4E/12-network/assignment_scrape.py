###############################################################
## File Name: assignment_scrape.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 12 - Network Programming 
## Excercise: Assignment 2 - GRADED
## Description: # Scraping Numbers from HTML using Beautiful Soup
## The program will use urllib to read the HTML 
## from the data files below, and parse the data, 
## extracting numbers and compute the sum of the 
## numbers in the file.
## 
## Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
## Actual data: http://py4e-data.dr-chuck.net/comments_1142516.html (Sum ends with 51)
#
## To run this, download the BeautifulSoup zip file
## http://www.py4e.com/code3/bs4.zip
## and unzip it in the same directory as this file
## Other References: n/a
###############################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
spans = soup('span')
total = 0
for span in spans:
    # Look at the parts of a tag
    # print('Span:', span)
    # print('class:', span.get('class', None))
    # print('Contents:', span.contents[0])
    total = total + int(span.contents[0])
    # print('Attrs:', tag.attrs)

print(total)