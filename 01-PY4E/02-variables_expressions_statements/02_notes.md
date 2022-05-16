__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 2 Notes
## Variables, Expressions, and Statements



A **value** is one of the basic things a program works with, like a letter or a number.

These values belong to different **types**:

- integer (1) 
- string ('yo')
- float (1.1)

Using comma separators for large integer values is not a legal integer in python (e.g. `print(1,000,0000)`). Python interprets 1,000,000 as a comma-separated sequence of integers.



A **variable** is a name that refers to a value. (Are Case Sensitive)

An **assignment statement** creates new variables and gives them values:



A **statement** is a unit of code that the Python interpreter can execute. We have seen two kinds of statements: print being an expression statement and assignment.

A *script* usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.



**Operators** are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called **operands**.

( +, -, *, / and ** )



An **expression** is a combination of values, variables and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions (assuming the variable x has been assigned a value)

If you type an expression in interactive mode, the interpreter *evaluates* it and displays the result.

> `>>> 1+1`
>
> `2`

But in a script, an expression all by itself doesn't do anything! *This is a common source of confusion for beginners.*



### 2.7 Order of Operations

Python follows PEDMAS / BEDMAS:

- **Parentheses** - have the highest precedence
- **Exponentiation**
- **Multiplication** and **Division** have the same precedence
- **Addition** and **Subtraction** have the same precedence
  - Operators with the same precedence are evaluated from left to right



### 2.8 Modulus Operator

The **modulus operator (%)** works on integers and yields the remainder when the first operand is divided by the second.



### 2.9 String Operations

The `+` operator works with strings, but it is not addition in the mathematical sense. Instead it performs concatenation.



### 2.10 Asking for User Input

Python provides a built-in function called `input` that gets input from the keyboard.

`input('Enter Something: ')`

`name = input('What is your name?\n')`

**\n** at the end represents a new line

Returns a string



