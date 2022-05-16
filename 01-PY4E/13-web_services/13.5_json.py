################################################################################
## File Name: 13.5_json.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: 13.5 Parsing JSON
## Description: Code walkthrough from book 
## Other References: n/a
################################################################################

import json

data = '''
[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Brent"
    }
]'''

info = json.loads(data)
print("User count:", len(info))

for item in info:
    print("Name", item['name'])
    print("ID", item['id'])
    print("Attribute", item['x'])