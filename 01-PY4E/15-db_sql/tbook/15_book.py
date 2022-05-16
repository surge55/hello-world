# Chapter 15 - Databases and SQL
# FROM THE TEXTBOOK

# Create a database file and table named "tracks" with two columns
# import sqlite3

# conn = sqlite3.connect('music.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Tracks')
# cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# conn.close()


# Put data into a database table
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES ("My Way", 15)')
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
print(cur)
for row in cur:
    print(row)


cur.execute('DELETE FROM Tracks Where plays < 100')
conn.commit()

cur.close