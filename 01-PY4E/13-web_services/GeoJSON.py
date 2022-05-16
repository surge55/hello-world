################################################################################
## File Name: GeoJSON.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: n/a
## Description: Using the Google Maps API (API Key on private server) 
## Other References: n/a
################################################################################

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    address = 'Ann Arbor, MI'
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=' + '*APIKEY*'
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

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    print('status=', js["status"])
