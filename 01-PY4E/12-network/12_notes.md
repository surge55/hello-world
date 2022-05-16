__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 12 Notes
## Networked Programs


### TCP Connections / Sockets

In computer networking, an internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the internet.



### TCP Port Number

- a port is an application-specific or process-specific software communication endpoint
- it allows multiple networked applications to coexist on the same server
- There is a list of well-known TCP port numbers https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers



### Sockets in Python

- Python has built-in support for TCP sockets

```python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80)) #host , port
```

Sockets are kind of like an unopened file handle, you have to connect/open it first. Creates a socket but does not associate it.



## Application Protocols

We need to decide and determine what kind of data we are going to send and receive from our socket.

Application Protocols

- mail
- world wide web
- etc...
- HTTP

### HTTP - Hypertext Transfer Protocol

- The dominant application layer protocol on the internet
- Invented for the web - to retrieve HTML, Images, Documents, etc.
- Extended to be data in addition to documents - RSS, Web Services, etc.
  - Basic concept
    - Make a connection - Request a document - Retrieve the document - Close the connection
- HTTP is the set of rules to allow browsers to retrieve web documents from servers over the internet



#### What is a Protocol?

- a set of rules that all parties follow so we can predict each other's behaviour
- and not bump into each other
  - on two-way roads in the US, drive on the right hand side of the road
  - on two-way roads in the UK, drive on the left hand side of the road

`http://www.dr-chuck.com/page1.html`

`http://` - protocol

`www.dr-chuck.com` - host

`/page1.html` - document



### Internet Standards

- The standards for all of the Internet protocols (inner workings) are developed by an organization
- Internet Engineering Task Force (IETF)
- www.ietf.org
- Standards are called "RFCs" - Request for Comments



**Making an HTTP request**

- Connect to the server like www.dr-chuck.com
- Request a document (or the default document)
  - Get URL HTTP/1.0
  - Get http://dr-chuck.com/page1.html HTTP/1.0



### Let's Write Web Browser

An HTTP Request in Python

```python
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while true:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysocket.close()
```



The output starts with headers which the web server sends to describe the document. After the server sends us the headers, it adds a blank line to indicate the end of the headers, and then sends the actual data of the file *romeo.txt*.

Sockets can be used to communicate with a web server or with a mail server or an other kind of server. **All that is needed is to find the document which describes the protocol and write the code to send and receive the data according to the protocol.**

The `encode()` and `decode()` methods convert strings into bytes objects and back again.

`encode` and `b''` are equivalent.

### Retrieving an Image over HTTP

 In the previous example, we retrieved a plain text file which had newlines in the file and we simply copied the data to the screen as the program ran. We can use a similar program to retrieve an image across using HTTP. Instead of copying the data to the screen as the program runs, we accumulate the data in a string, trim off the headers and then save the image data to a file as follows:

```python
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'Get http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
```





