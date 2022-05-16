__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 13 Notes
## Using Web Services

### Data on the Web

-  With HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
- We needed to come up with an agreed way to represent data going between applications and across networks
- There are two commonly used formats: XML and JSON

*Wire Protocol* that is independent of any programming language.



## XML - eXtensible Markup Language

- Primary purpose is to help information systems share structured data
- It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible



### XML Terminology

**Tags** indicate the beginning and ending of elements

**Attributes** - Keyword/value pairs on the opening tag of XML

**Serialize/De-Serialize** - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

### XML Schema

- Describing a "contract" as to what is acceptable XML
- Description of the legal format of an XML document
- Expressed in terms of constraints on the structure and content of documents
- Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema"
- If a particular piece of XML meets the specification of the Schema - it is said to be "validate"

You have two pieces of software talking to one another - who is right if there is a conflict. You would setup a "contract" between the two applications.



### Many XML Schema Languages

- Document Type Definition (DTD)
- Standard Generalized Markup Language (ISO 8879:1986 SGML)
- **XML Schema from W3C - (XSD)**
  - We will focus on the W3C version
  - It is often called "W3C Schema" because "Schema" is considered generic
  - More commonly it is called XSD because the file names end in .xsd



### XSD Structure

``` xml
# XML document to be checked
<person>
	<lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person>
```

- **xs: element** 

- **xs: sequence**

- **xs: complexType**

  ```xml
  # Structure to be confirmed with
  
  <xs:complexType name="person">
      <xs:sequence>
          <xs:element name="lastname" type="xs:string"/>
          <xs:element name="age" type="xs:integer"/>
          <xs:element name="dateborn" type="xs:date"/>
      </xs:sequence>
  </xs:complexType>
  ```



**Date Formats**

It is common to represent time in UTC/GMT, given that servers are often scattered around the world.

ISO 8601

2002-05-30T09:30:10Z

T - Time

Z - Zulu / UTC / GMT (time zone)





## JSON - JavaScript Object Notation 

More common on the net. XML is better for structured data. Jason easier to just get data out of a system.

JSON.org

Actually is derived from the JS literal syntax.



```python
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

info = json.loads(data)		# info is a dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
```

JSON represents data as nested "lists" and "dictionaries".

JSON returns a dictionary or a list.

 

```python
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

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
```



## Service Oriented Architecture

- Most non-trivial web applications use services
- They use services from other applications
  - credit card charge
  - hotel reservation systems
- Services publish the "rules" applications must follow to make use of the service (API)



### Multiple Systems

- Initially - two systems cooperate and split the problem
- As the data/service becomes useful - multiple applications want to use the information / application



## Application Program Interface

The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface. The software that provides the functionality described by an API is said to be an "implementation" of the API. An API is typically defined in terms of the programing used to build an application.

http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI



### API Security and Rate Limiting

- The compute resources to run these APIs are not "Free"
- The data provided by these APIs is usually valuable
- The data providers might limit the number of requests per day, demand an API "key", or even charge for usage
- They might change the rules as things progress...



## Summary (video)

- Service Oriented Architecture - allows an application to be broken into parts and distributed across a network
- An API is contracted for interaction
- Web Services provide infrastructure for applications cooperating (an API) of over a network - SOAP and REST are two styles of web services
- XML and JSON are serialized formats



\

\

\

From Textbook

\

\

\



# Using Web Services



One communication over HTTP became common, we started producing documents that were specifically designed to be consumed by other programs (i.e. not HTML to be displayed in a browser).



Two common formats when exchanging data across the web:

**XML** - has been in use for a very long time and is best suited for exchanging document-style data.

**JSON** - Used when programs just want to exchange dictionaries, lists or other internal information with each other (JavaScript Object Notation).



### XML - eXtensible Markup Language

Looks very similar to HTML, but XML is more structured than HTML. Example:

```xml
<person>
	<name>chuck</name>
    <phone type="intl">
    	+1 734 303 4456
    </phone>
    <email hide="yes" />
</person>
```



Each pair of opening and closing tags (<person>...</person>) represents an *element* or *node* with the same name as the tag. Each element can have some text, some attributes (e.g. hide), and other nested elements. If an XML element is empty (i.e. has no content), then it may be depicted by a self-closing tag (e.g. <email />). Think of XML as a tree structure.

```python
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
```



`'''` and `"""` allow for the creation of strings that span multiple lines in python.

Calling `fromstring` converts the string representation of the XML into a 'tree' of XML elements. When the XML is in a tree, we have a series of methods we can call to extract portions of data from the XML string. The `find` function searches through the XML tree and retrieves the element that matches the specified tag.

``` python
# 13.3 Looping through nodes
# Often XML has multiple nodes and we need to write a loop to process all of the nodes. 
# In the following program, we loop through all of the user nodes:>

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
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #returns a list object?
print('User count:', len(lst))
# print(type(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get('x'))
```



The `findall` method retrieves a Python list of subtrees that represent the user structure in the XML tree. Then we can write a `for` loop that looks at each of the user nodes and prints the name and id text elements as well as the x attribute for the user node.

It is important to include all parent level elements in the `findall` statement except for the top level element (e.g. `users/user`). Otherwise, Python will not find any desired nodes.

`lst` stores all users elements that are nested within their users parent. `lst2 = stuff.findall('user')` looks for users elements that are not nested within the top level stuff element where there are none.





### JavaScript Object Notation - JSON

The JSON format was inspired by the object and array format used in the JavaScript language. But since Python was invented before JavaScript, Python's syntax for dictionaries and lists influenced the syntax of JSON. So the format of JSON is nearly identical to a combination of Python Lists and Dictionaries.

Here is a JSON encoding that is roughly equivalent to the XML above:

```json
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
```

- In JSON we add attributes as simple **key-value pairs**.
- The XML "person" tag is gone, replaced by a set of outer curly braces.



In general, JSON structures are simpler than XML because JSON has fewer capabilities than XML. But JSON has the advantage that it maps directly to some combination of dictionaries and lists. And since nearly all programming languages have something equivalent to Python's dictionaries and lists, JSON is a very natural format to have two cooperating programs exchange data.

JSON is quickly becoming the format of choice for nearly all data exchange between applications because of its relative simplicity to XML.



### Parsing JSON

We construct our JSON by nesting dictionaries and lists as needed. In this example, we represent a list of users where each user is a set of key-value pairs (a dictionary). So we have a list of dictionaries.

In the following program, we use the built-in `json` library to parse the JSON and read through the data. Compare this closely to the equivalent XML data and code above. **The JSON has less detail, so we must know in advance that we are getting a list and that the list is of users and each user is a set of key-value pairs.** The JSON is more succinct (an advantage) but also is less self-describing (a disadvantage).

```python
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
```



If you compare the code you will see that what we get from `json.loads()` is a Python list which we traverse with a `for` loop, and each item within that list is a Python dictionary. Once the JSON has been parsed, we can use the Python index operator to extract the various bits of data for each user. We don't have to use the JSON library to dig through the parsed JSON, since **the returned data is simple native Python structures**.



In general, the industry is trending away from XML and towards JSON for web services. XML is more self-descriptive than JSON and so there are some applications where XML retains an advantage. For example, most word processors store documents internally using XML rather than JSON.



### Application Programming Interfaces

We now have the ability to exchange data between applications using HTTP and a way to represent complex data that we are sending back and forth between these applications using XML or JSON.

The next steps is to begin to define and document "contracts" between applications using these techniques. The general name for these application-to-application contracts is **Application Programming Interfaces (APIs)**. When we use an API, generally one program makes a set of services available for use by other applications and publishes the API (i.e. the rules) that must be followed to access the services provided by the program.

When we begin to build our programs where the functionality of our program includes access to services provided by other programs, we call the approach a **Service Oriented Architecture (SOA)**. A SOA approach is one where our overall application makes use of the services of other applications. A non-SOA approach is where the application is a single standalone application which contains all of the code necessary to implement the application.

SOA advantages:

1. we always maintain only one copy of data (this is particularly important for things like hotel reservations where we do not want to over-commit)
2. the owners of the data can set the rules about the use of their data

When an application makes a set of services in its API available over the web, we call these **web services**.



### Security and API Usage

Its is common to require an API key in order to access or use a vendor's API. 

Sometimes once you get your API key, you simple include the key as part of POST data (sending data over HTTP to the server with the request) or perhaps as a parameter on the URL when calling the API (Google).

Other times, the vendor wants increased assurance of the source of the requests and so they expect you to send cryptographically signed messages using shared keys and secrets. A very common technology that is used to sign requests over the internet is called **OAuth**.

