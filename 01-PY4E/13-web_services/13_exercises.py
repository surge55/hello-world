###############################################################
## File Name: 13_exercises.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: n/a
## Description: Code walkthrough from book 
## Other References: n/a
###############################################################

# XML WORKED EXAMPLE
import xml.etree.ElementTree as ET  #built in XML parser

# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''


# tree = ET.fromstring(data)

# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))


# # Next Example - XML
# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user') # returns a list of tags that match
# print('User Count:',len(lst))
# # print(lst)

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get("x"))


## JSON - outer brace makes this a dictionary
import json
data = '''{
	"name" : "Chuck",
	"phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
	},
	"email" : {
		"hide" : "yes"
	}
}'''

info = json.loads(data)     # info is a dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

## JSON - outer bracket makes this a List
import json
input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {   "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

info = json.loads(input)        # info is a list
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
