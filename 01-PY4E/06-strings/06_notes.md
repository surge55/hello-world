__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 6 Notes
## Strings

__From Lecture__
### Looking in Strings

- WE can get any single character in a string using an index specified in square brackets
- The index value must be an integer and starts at zero
- The index value can be an expression that is computed
- You will get a python error if you attempt to index beyond the end of a string
- So be careful when constructing index values and slices
- Strings have lengths (use `len`)



### Looping Through Strings

- Using a while statement and in iteration variable and the `len` function, we can construct a loop to look at each of the letters in a string individually.
- A definite loop using a `for` statement is much more elegant
- The iteration variable is completely taken care of by the `for` loop

```python
fruit = 'banana'
for letter in fruit:
    print(letter)
    
# VS. (poorer construct)
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
```



### Looking Deeper into `in`

- The iteration variable "iterates" through the sequence (ordered set)
- The block (body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in the sequence





### Slicing String

- We can also look at any continuous section of a string using a colon separator
- **The second number is one beyond the end of the slice - "up to not including"**
- If the second number is beyond then end of the string, it stops at the end
- If we leave off the first number or the last number of the slice it is assumed to be the beginning or the end of the string respectively



### Using in as a logical operator

```python
fruit = 'banana'
'n' in fruit
>>> True
```



### String Comparison

Behave naturally except in caps/punctuation depends on charset of local machine



### String Library

- Python has a number of string functions which are in the string library
- These functions are already built into every string - we invoke them by appending the function to the string variable
- These functions do not modify the original string, instead they return a new string that has been altered

```python
>>> greet = 'Hello Bob'
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print('Hi There'.lower())
hi there
```



Anything that is of type "str" (String), can use the string library.

```py
>>> stuff = 'Hello World'
>>> type(stuff)
<class'str'>
```

To list all the methods of a string (`str`) use the `dir()` function. Or go to the python documentation: https://docs.python.org/3/library/stdtypes.html#string-methods



### Searching a String

- We use the `find()` functions to search for a substring within another string
- `find()` finds the first occurrence of the substring, and returns the index position of the occurrence
- If the substring is not found, `find()` returns -1



# From Textbook



You can use negative indices, which count backward from the end of the string. The expression `fruit[-1]` yields the last letter, `fruit[-2]` yields the second to last, and so on.



### Format Operator

The format operator `%` allows us to construct strings, replacing parts of the strings with the data stored in variables. When applied to integers `%` is the modulus operator. But when the first operand is a string, `%` is the format operator.

For example, the form at sequence `%d` means that the second operand should be formatted as an integer ("d" stands for "decimal"):

```python
>>> camels = 42
>>> '%d' % camels
'42'
```

The result is the sting '42', which is not to be confused with the integer value 42. A format sequence can appear anywhere in the string, so you can embed a value in a sentence:

```py
>>> camels = 42
>>> "I have spotted %d camels." % camels
"I have spotted 42 camels."
```

If there is more than one format sequence in the string, the second argument to be a tuple. Each format sequence is matched with an element of the tuple, in order

The following example uses `%d` to format an integer, `%g` to format a floating-point number, and `%s` to format a string.

```py
>>> "In %d years I have spotted %g %s/" % (3, 0.1, "camels")
'In 3 years I have spotted 0.1 camels/'
```

