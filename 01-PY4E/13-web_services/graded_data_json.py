################################################################################
## File Name: graded_data_json.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: 1
## Description: Extracting Data From JSON - submitted to Autograder 
## Other References: n/a
################################################################################


import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location:')
    # address = "http://py4e-data.dr-chuck.net/comments_42.json" # TEST
    # address = "http://py4e-data.dr-chuck.net/comments_1142519.json" # ACTUAL
 
    if len(address) < 1: break
    url = address

    # Count and Sum Exercise
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    # print('count:', len(info))
    # print(info["comments"])

    count = 0
    sum = 0
    for item in info["comments"]:
        count += 1
        sum = int(item["count"]) + sum
    
    print("Count:", count)
    print("Sum:", sum)

    # testing/print
    # print(data.decode())
    # tree = ET.fromstring(data)

    # results = tree.findall('result')
    
    # counts = tree.findall('.//count')

    # total = 0
    # sum = 0
    # for tag in counts:
    #     total += 1
    #     sum = int(tag.text) + sum    
    # # print(results)
    # print('Count:', total)
    # print('Sum:', sum)



url = input("Enter location: ")

