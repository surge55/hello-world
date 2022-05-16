################################################################################
## File Name: 15_exercises.py
## File Type: Python File
## Author: surge55
## Course: Python 4 Everybody
## Chapter: Chapter 15 - Databases and SQL 
## Excercise: n/a
## Description: Code walkthrough from book and lecture
## Other References: n/a
################################################################################

## FROM LECTURE
# emaildb.py

# import sqlite3

# # make a connection
# conn = sqlite3.connect('emaildb.sqlite') # will create the DB if it doesn't exist
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]

#     cur.execute('SELECT count FROM Counts WHERE Email = ? ', (email,))  # ? is placeholder to prevent SQL injection and entering incorrect text from user entered data / (email,) is single tuple --> you could have more ? to insert more data 
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('INSERT INTO Counts (email, count) VALUES (?,1)', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
#     conn.commit()

# # read the database
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()


# FROM LECTURE
# twspider.py

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter 
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 Limit 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieeved Twitter accounts found')
            continue
url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
print('Retrieving', url)
connection = urlopen(url, context=ctx)
data = connection.read().decode()
headers = dict(connection.getheaders())

print('Remaining', headers['x-rate-limit-remaining'])
js = json.loads(data)
# Debugging
# print(json.dumps(js, indent=4))

cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct,))

countnew = 0
countold = 0
for u in js['users']:
    friend = u['screen_name']
    print(friend)
    cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Twitter SET friends = ? WHERE name =?', (count+1, friend))
        countold = countold + 1
    except:
        cur.execute('INSERT INTO Twitter (name, retrieved, firends) VALUES (?, 0, 1)',(friend,))
        countnew += 1

print('New accounts=', countnew, ' retrieved=', countold)
conn.commit()


