################################################################################
## File Name: graded_json_api.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services
## Excercise: 3
## Description: Calling a JSON API (GeoJSON). Using the Google Maps API 
## Other References: n/a
################################################################################

# Calling a JSON API# GeoJSON
# Using the Google Maps API

import urllib.request, urllib.parse, urllib.error
import json

# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    # address = 'South Federal University'
    # address = 'Franklin Pierce College'
    
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=' + '42'
    # print(url)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print("==== Failure to Retrieve ====")
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    print('Place id', js["results"][0]["place_id"])
