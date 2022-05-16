###############################################################
## File Name: 13_exercise1.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: 1
## Description: Change geojson.py to print out the two charater country code from the retrieved data.
## Add error checking so your program does not traceback if the country code is not there.
## Once you have it working, serach for "Atalantic Ocean" and make sure it can handle locations
## that are not in any country
## Other References: n/a
###############################################################

# GeoJSON
# Using the Google Maps API

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    # address = 'Ann Arbor, MI'
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=' + 'AIzaSyD4BTmQAggsS6pvgjNIptFrm6OsXJRkOVQ'
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

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print('lat', lat, 'lng', lng)
    
    # Exercise 1 Code
    
    try:
        location = js['results'][0]['address_components'][3]["short_name"]
        if len(location) != 2:
            location = "None"
    except:
        location = "None"
    print("Country Code:", location)
