__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 15 Notes
## Using Databases and SQL


From LECTURE



## Relational Databases and SQL Lite

https://sqlitebrowser.org/





### Relational Databases

Relational databases model data by storing rows and columns in tables. The power of the relational database lies in its ability to efficiently retrieve data from those tables and in particular where there are multiple tables and the relationships between those tables involved in the query.

(weren't that popular early - and were slower and used advanced mathematics)



**Database** - contains many tables

**Relation (or table)** - contains tuples and attributes

**Tuple (or row)** - a set of fields that generally represent an "object" like a person or a music track

**Attribute (also column or field** - one of possibly many elements of data corresponding to the object represented by the row



### SQL - Structured Query Language

Is the language we used to issue commands to the database

- Create a table
- Retrieve some data
- Update/Insert data 
- Delete data

**<u>CRUD</u>**



### Web Applications with Databases

- **Application Developer** - Builds the logic for the application, the look and feel of the application - monitors the application for problems
- **Database Administrator** - Monitors and adjusts the database as the program runs in production
  - A DBA is a person responsible for the design, implementation, maintenance, and repair of an organization's database. The role includes the development and design of database strategies, monitoring and improving database performance and capacity, and planning for future expansion requirements. They may also plan, coordinate, and implement security measures to safeguard the database
- Often both people participate in the building of the "Data model"



### Database Model

A **database model** or **database schema** is a the <u>structure of format of a database</u>, describe in a formal language supported by the database management system. In other words, a "database model" is the application of a data model when used in conjunction with a database management system.



### Common Database Systems

Three major database management systems in wide use:

- **Oracle** - Large, commercial, enterprise-scale, very very tweakable
- **MySQL** - Simpler but very fast and scalable - commercial open source
- **SQL Server** - Very nice from Microsoft (also Access)
- Others: HSQL, SQL Lite, Postgres, MariaDB, MongoDB...

SQLite is an embedded database system and is common bundled in a lot of software.



#### SQLite Browser

- SQLite is a very popular database - it is free and fast and small
- SQLite Browser allows us to directly manipulate SQLite files
- SQLite is embedded in Python and a number of other languages



### Lets Make a Database

Create Table Statement in SQL - created using UI in SQLite Browser

```sqlite
CREATE TABLE "Users" ("name" TEXT, "email" TEXT)
```



**SQL: Insert**

```sqlite
INSERT INTO Users(name, email) VALUES ('Kristin', 'kf@ubc.edu')
```



**SQL: Delete**

```sqlite
DELETE FROM Users WHERE email='ted@umich.edu'
```



**SQL: Update**

```sqlite
UPDATE Users SET name="CHUCK" WHERE email='csev@py4e.edu'
```



**Retrieving Records: Select**

- The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause

```sqlite
SELECT * FROM Users
Select * FROM Users WHERE email='csev@py4e.edu'
```



**Sorting with ORDER BY**

- You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order

```sqlite
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name DESC
```



### This is not too exciting (so far)

- Tables pretty much look like big fast programmable spreadsheets with rows, columns and commands
- The power comes when we have more than one table and we can exploit the relationships between tables



## Complex Data Models & Relationships



### Database Design

- Database design is an art form of its own with particular skills and experience
- Our foal is to avoid the really bad mistakes and design clean an easily understood databases
- Others may performance tune things later
- Database design starts with a picture...

![image-20210920151456955](C:\Users\SrdjanManojlovic\AppData\Roaming\Typora\typora-user-images\image-20210920151456955.png)



### Building a Data Model

- Draw a picture of the data objects for our application and then figuring out how to represent the objects and their relationships
- Basic Rule: Don't put the same string data in twice - use a relationship instead
- When there is one thing in the "Real World" there should be one copy of that thing in the database



**Build a Music Management Application**

- Track
- Length
- Artist
- Album 
- Genre
- Rating
- Count



## For Each 'piece of info...'

- Is the Column an object or an attribute of another object?
- Once we define objects, we need to define the relationships between objects.



**Tables**

Track (len, rating, count)

Album

Artist

Genre



**Relationship Model**

Track --> Album ---> Artist

Track --> Genre





### Representing Relationships in a Database

**Database Normalization (3NF**)

- There is *tons* of database theory - way too much to understand without excessive predicate calculus
- Do not replicate data - reference data - point at data
- Use integers for keys and for references
- Add a special "key" column to each table which we will make references to. By convention, many programmers call this column "id"



**Integer Reference Pattern**

- We use integers to reference rows in another table



**Three Kinds of Keys**

- **Primary Key** - generally an integer auto-increment field
- **Logical Key** - what the outside world uses for lookup
- **Foreign Key** - generally an integer key pointing to a row in another table
  - A foreign key is when a table has a column that contains a key which points to the primary key of another table
  - When all primary keys are integers, then all foreign keys are integers - this is good - very good

| Album Table | Type    | Key Type    |
| ----------- | ------- | ----------- |
| id          | integer | primary key |
| title       | text    | logical key |
| artist_id   | integer | foreign key |
| ...         | ...     | ...         |



**Key Rules**

Best Practices

- Never use your logical key as the primary key
- Logical keys can and do change, albeit slowly
- Relationships that are based on matching string fields are less efficient than integers



## Using Join Across Tables



**The JOIN Operation**

- The JOIN operation links across several tables as part of a select operation
- You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause



`table.field` format convention



## Many-to-Many Relationships

- Sometimes we need to model a relationship that is many-to-many
- We need to add a "connection" (junction table) table with two foreign keys
- There is usually no separate primary key



### Complexity Enables Speed

- Complexity makes speed possible and allows you to get very fast results as the data size grows
- By normalizing the data and linking it with integer keys, the overall amount of data which the relational database must scan is far lower than if the data were simply flattened out
- It might seem like a tradeoff - spend some time designing your database so it continues to be fast when your application is a success



### Additional SQL Topics

**Indexes** - improve access performance for things like string fields

**Constraints** - on data - (cannot be NULL, etc.)

**Transactions** - allow SQL operations to be grouped and done as a unit



\

\

\ 

\\\\\\\\\\\\\\\\\ FROM TEXTBOOK \\\\\\\\\\\\\\\\\\\\\\\\\

\

\

\





## What is a database?

A *database* is a file that is organized for storing data. Most databases are organized like a dictionary in the sense that they may keys to values. The biggest difference is that the database is on a disk, so it persists after the program ends. Because a database is stored on permanent storage, it can store far more data than a dictionary, which is limited to the size of memory in the computer.

Database software maintains its performance by building *indexes* as data is added to the database to allow the computer to jump quickly to a particular entry.



## Database Concepts

Looks like a spreadsheet. The primary data structures in a database are: *tables, rows* and *columns*.

In technical descriptions of relational databases the concepts of table, row and column are more formally referred to as: *relation, tuple, attribute*.



## Database Browser for SQLite

To work with data in SQLite database files, many operations can be done more conveniently using software called the Database Browser for SQLite.

www.sqlitebrowser.org

Using the browser you can easily create tables, insert data, edit data, or run simple SQL queries on the data in the database.



## Creating a Database Table

Databases require more defined structure than Python lists or dictionaries.

When creating a database table, we must tell the database in advance the names of each of the columns in the table and type of data which we are planning to store in each column. When the database software knows the type of data in each column it can choose the most efficient way to store and look up the data based on the type of data.



The code to create a database file and a table named "Tracks" with two columns in the database is as follows:

```python
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
```



`conn = sqlite3.connect('music.sqlite')`

The connect operation makes a "connection" to the database stored in the file '**music.sqlite**' in the current directory. If the file does not exist, it will be created. The reason this is called a "connection" is that sometimes the database is stored on a separate "database server" from the server on which we are running out application. In our simple examples the database will just be a local file in the same directory as the Python code we are running.

A *cursor* is like a file handle that we can use to perform operations on the data stored in the database. Calling `cursor()` is very similar conceptually to calling `open()` when dealing with text files.



![image-20210921093729421](C:\Users\SrdjanManojlovic\AppData\Roaming\Typora\typora-user-images\image-20210921093729421.png)

Once we have the cursor, we can begin to execute commands on the contents of the database using the `excute()` method.

Database commands are expressed in SQL.

Two SQL commands executed in our database. To run multiple statements use `.executescript()` method.



`cur.execute('DROP TABLE IF EXISTS Tracks')`

The first SQL command removes the Tracks table from the database if it exists. This pattern is simply to allow us to run the same program to create the Tracks table over and over again without causing an error. Note that the DROP TABLE command deletes the table and all of its contents from the database (i.e. there is no "undo")



`cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')`

The second command creates a table named Tracks with a text column named title and an integer column named plays.



Now that we have created a table named Tracks, we can put some data into that table using the SQL INSERT operation. Again, we begin by making a connection to the database and obtaining the cursor. We can then execute SQL commands using the cursor.

The SQL INSERT command indicates which table we are using and then defines a new row by listing the fields we want to include (title, plays) followed by the VALUES we want placed in the new row. We specify the values as questions marks **(?, ?)** to indicate that the actual values are passed in as a tuple ('My Way', 15) as the second parameter to the `execute()` call.



```python
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES ("My Way", 15)')

conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)


cur.execute('DELETE FROM Tracks Where plays < 100')
conn.commit()

cur.close
```



First we INSERT two rows into our table and use `commit()` to force the data to be written to the database file.

Then we use the SELECT command to retrieve the rows we just inserted from the table. On the SELECT command, we indicate which columns we would like (title, plays) and indicate which table we want to retrieve the data from. After we execute the SELECT statement, the cursor is something we can loop through in a for statement. For efficiency, the cursor does not read all of the data from the database when we execute the SELECT statement. Instead, the data is read on demand as we loop through the rows in the for statement.

**Output:**

> Tracks:
>
> ('Thunderstruck', 20)
>
> ('My Way', 15)

Our for loop finds two rows, and each row is a Python tuple with the first value as the title and the second value as the number of plays.

*Note: you may see strings starting with u' in other books or on the internet. This was an indication in Python 2 that the strings are Unicode strings that are capable of storing non-Latin character sets. In Python3, all strings are Unicode strings are Unicode strings by default.* 

At the very end of the program, we execute an SQL command to DELETE the rows we have just created so we can run the program over and over. The DELETE command shows the use of a WHERE clause that allows us to express a selection criterion so that we can ask the database to apply the command to only the rows that match the criterion.



## Structured Query Language Summary

SQL is standardized across many different database vendors.

Using `*` indicates that you want the database to return all of the columns for each row that matches the WHERE clause.

Note, unlike Python, in SQL WHERE clause we use a single equal sign to indicate a test for equality rather than a double equal sign. Other logical operations allowed: `<, >, >=, <=, !=, AND, OR` and parentheses.

It is possible to UPDATE a column or columns within one or more rows in a table using the **SQL UPDATE** statement:

`UPDATE Tracks SET plays = 16 WHERE title = 'My Way'`

The UPDATE statement specifies a table and then a list of fields and values to change after the SET keyword and then an optional WHERE clause to select the rows that are to be updated. A single UPDATE statement will change all of the rows that match the WHERE clause. If a WHERE clause is not specified, if performs the UPDATE on all of the rows in the table.



**`INSERT, SELECT, UPDATE, DELETE`**

The four basic SQL commands that allow the four basic operations needed to create and maintain data.



## Spidering Twitter using a Database

One of the problems of any kind of spidering program is that it needs to be able to be stopped and restarted many times and you do not want to lose the data that you have retrieved so far. You don't want to always restart your data retrieval at the very beginning so we want to store data as we retrieve it so our program can start back up and pick up where it left off.

.... not reviewed...



## Basic Data Modeling

The real power of a relational database is when we create multiple tables and make links between those tables. The act of deciding how to break up your application data into multiple tables and establishing the relationships between the tables is called **data modeling**. The design document that shows the tables and their relationships is called a **data model**.

Data modeling is a relatively sophisticated skill.

String duplication data violates one of the best practices for database normalization which basically states that we should never put the same string data in the data base more than once. If we need the data more than once we create a numeric key for the data and reference the actual data using this key.

In practical terms, a string takes up a lot more space than an integer on the disk and in memory of our computer, and takes more processor time to compare and sort. If we only have a few hundred entries, the storage and processor time hardly matters. But if we have a million people in our database and a possibility of 100 million friend links, it is important to be able to scan data as quickly as possible.

 SQLite has a feature that automatically adds the key value for any row we insert into a table using a special type of data column (INTEGER PRIMARY KEY)

`CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)`

We also add the keyword UNIQUE to indicate that we will not allow SQLite to insert two rows with same value for name.

`CREATE TABLE Follows(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))`

We create a tabled called Follows with two integer columns and a constraint on the table that the combination of from_id and to_id must be unique in this table.

When we add UNIQUE clauses to our tables we are communicating  a set of rules that we are asking the database to enforce when we attempt to insert records. We are creating these rules as a convenience in our programs. The rules both keep us from making mistakes and make it simpler to write some of our code.



## Programming with Multiple Tables

We indicate that the name column in the People table must be UNIQUE. We also indicate that the combination of the two numbers in each row of the Follows table must be unique. These constraints keep us from making mistakes such as adding the same relationship more than once.

We can take advantage of these contraints in the following code:

`cure.execute('''INSERT OR IGNORE INTO People (name, retrieved) VALUES ( ? , 0)''', (friend,))`

We add thee OR IGNORE clause to our INSERT statement to indicate that if this particular INSERT would cause a violation of the "name must be unique" rule, the database system is allowed to ignore the INSERT. We are using the database constraint as a safety net to make sure we don't inadvertently do something incorrect.

Similarly, the following code ensures that we don't add the exact same Follows relationship twice.

**JOIN**

The result of the JOIN is to crate extra-long "metarows" which have both the fields from the People table and the matching fields from the Follows table. Where there is more than one match between id fields in each table the JOIN creates a metarow for each of the matching pairs of rows, duplicating data as needed.