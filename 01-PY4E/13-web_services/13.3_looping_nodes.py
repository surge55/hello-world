################################################################################
## File Name: 13.3_looping_nodes.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services 
## Excercise: 13.3 Looping through nodes
## Description: # Often XML has multiple nodes and we need to write a loop to 
## process all of the nodes. 
## In the following program, we loop through all of the user nodes: 
## Other References: n/a
################################################################################


import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
    <user>Srdj</user>
</stuff>'''


stuff = ET.fromstring(input)

# EXPLORE ground
# lst2 = stuff.findall('users/user')
# print('User count:', len(lst2))
# lst3 = stuff.findall('user')
# print('User count:', len(lst3))



lst = stuff.findall('users/user') #returns a list object?
print('User count:', len(lst))
# print(type(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get('x'))