###############################################################
## File Name: 13.2_pasing-xml.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 13 - Web Services
## Excercise: 13.2
## Description: Simple application that parses some XML and 
## extracts some data elmeents from the XML
## Other References: n/a
###############################################################

# 13.2 Parsin XML
# Simple application that parses some XML and extracts some data elmeents from the XML

import xml.etree.ElementTree as ET #xml tree is depreicated due to security risks

data = '''
<person>
	<name>chuck</name>
    <phone type="intl">
    	+1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
