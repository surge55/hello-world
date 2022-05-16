__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 1 Notes
## Why should you learn to write programs?


### Preface

This book is a remix on "Think Python: How to Think Like a Computer Scientist" by Allen B. Downey, Jeff Elkner and others.

Students who find this book useful and want to further explore should look at the Think Python book.



# Chapter 1

# Why should you learn to write programs?





An **interpreter** reads the source cod of a program as written by the programmer, parses the source code, and interprets the instructions on the fly. Python is an interpreter and when we are running Python interactively, we can type a line of Python (a sentence) and Python processes it immediately and is ready for us to type another line of Python.

A **compiler** needs to be handed the entire program in a file, and then it runs a process to translate the high-level source code into machine language and then the compiler puts the resulting machine language into a file for later execution. (E.g. .exe or .dll files in Windows)



The **Python Interpreter** is written in a high-level language called "C". The source code is available on www.python.org. So python is a program itself and it is compiled into machine code.



### 1.9 The Building Blocks of Programs



Conceptual patterns that are used to construct programs. These constructs are not specific to Python, they are a part of every programming language from machine language up to the high-level languages.

**input** 		Get data from the "outside" worlds. This might be reading data from a file, or even some kind of 					sensor like a microphone or GPS. In our initial programs, our input will come from the user 					typing data on the keyboard.

**output**		Display the results of the program on a screen or store them in a file or perhaps write them to 					a device like a speaker.

**sequential execution** 	Perform statements one after another in the order they are encountered in the script

**conditional execution** Check for certain conditions and then execute or skip a sequence of statements

**repeated execution** Perform some set of statements repeatedly, usually with some variation.

**reuse**		Write a set of instructions once and give them a name and then reuse those instructions as needed throughout your program



### 1.10 What could possibly go wrong?



**Syntax Errors:**

- Indicates that you have violated the "grammar" rules of Python
- Python tries to point you to the line and character where it noticed the error
- The line where the error occurs could be earlier in your Python program
- Easiest to fix



**Logical Errors:**

- Occurs when you have correct syntax but there is a mistake in the order of the statements or perhaps a mistake in how the statements relate to one another
- For Example: "take a drink from your water bottle, put it in your backpack, walk to the library, and then put the top back on the bottle"



**Semantic Errors:**

- Occurs when your description of the steps to take is syntactically perfect and in the right order, but there is simply a mistake in the program
- The program is perfectly correct but it doesn't do what you *intended* it to do



### 1.11 Debugging

Debugging is the process of finding the cause of the error in your code. There are 4 things to try:

**reading** - examine your code, read it back to yourself, and check that it says what you meant

**running** - experiment by making changes and running different versions. Often if you display the right thing at the right place in the program, the problem becomes obvious, but sometimes you have to spend some time to build scaffolding.

**ruminating** - Take some time to think! What kind of error is it: syntax, runtime, semantic? What information can you get from the error messages, or from the output of the program? What kind of error could cause the problem you're seeing? What did you change last, before the problem appeared?

**retreating** - At some point, the best thing to do is back off, undoing recent changes, until you get back to a program that works and that you understand. Then you can start rebuilding.







## 1.14 EXERCISE



Too Simple to Record 





