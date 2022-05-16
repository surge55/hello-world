__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 7 Notes
## Files

__From Lecture__

File Processing text files. A text file can be though of as a sequence of lines.



### Open a file

`open()`(filename, mode)

mode r is for read

mode w is for write



A text file has  **newlines** `\n` at the end of each line in the file.



### Read Files in Python

File Handle as a Sequence

- A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
- We can use the for statement to iterate through a sequence
- Remember - a sequence is an ordered set



## 7.2 Opening Files

Opening a file communicates with your operating system, which knows where the data for each file is stored. When you open a file, you are asking the OS to find the file by name and make sure it exists. The file should be saved in the same file location as where you are executing the python file from.

```py
>>> fhand = open("mbox.txt")
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>
```

If the open is successful, the operating system returns a ***file handle***. The file handle is not the actual data contained in the file, but instead it is a "handle" that we can use to read the data. You are given a handle if the requested file exists and you have the proper permissions to read the file.



## 7.4 Reading Files

It is a good idea to store the output of `.read()` as a variable because each call to read exhausts the resource:

```py
>>> fhand = open('mbox-short.txt')
>>> print(len(fhand.read()))
94626

# better to use a variable
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
```

Remember that this form of the `open` function should only be used if the file data will fit comfortably in the main memory of your computer. If the file is too large to fit in main memory, you should write your program to read the file in chunks using a for or while loop.



## 7.5 Searching through a file

We can combine the patter for reading a file with string methods to build simple search mechanisms. We can use the string method `.startswith()` to select only those lines with a desired prefix.

User `.rstrip()` to remove extra newline characters.

`line = line.rstrip()`



## 7.7 Using try, except and open

The `exit()` function terminates the program. It is a function that we call that never returns. Now when our users (or QA team) types in silliness or bad file names, we "catch" them and recover gracefully.



## 7.8 Writing Files

To write a file, you have to open it with mode "w" as a second parameter:

```py
>>> fout = open('output.txt', 'w')
>>> print(fout)
```

If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful!. If the file doesn't exist, a new one is created.

The **write** method of the file handle object puts data into the file, returning the number of characters written. The default write mode is text for writing (and reading) strings.

```py
>>> line1 = "this here's the wattle,\n"
>>> fout.write(line1)
24
```

We must make sure to manage the ends of lines as we write to the file by explicitly inserting the newline character when we want to end a line. The print statement automatically appends a new line, but the write method does not add the newline automatically.

When you are done writing, you have to close the file to make sure that the last bit of data is physically written to the disk so it will not be lost if the power goes off.

`>>> fout.close()`

We could close the files which we open for read as well, but we can be a little sloppy if we are only opening a few files since Python makes sure that all open files are closed when the program ends. When we are writing files, we want to explicitly close the files so as to leave nothing to chance.

