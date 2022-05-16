__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


## Chapter 8 Notes
## Lists



**Algorithms**

- a set of rules or steps used to solve a problem

**Data structures**

- a particular way of organizing data in a computer
- lists is a type of data structure (so are strings)



**A List is a kind of Collection**

- a collection allows us to put many values in a single 'variable'
- a collection is nice because we can carry all many values around in one convenient package



**List Constants**

- A list element can be any python object, even another list
- A list can be empty



**Lists are Mutable**

- strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any changes

- Lists are "mutable" - we can change an element of a list using the index operator

- You can concatenate lists

- Lists can be sliced:

  - Starts at zero

  - Just like in strings, the second number is "up to but not including"

  - ```py
    t = [9, 41, 12, 3, 74, 15]
    t[1:3]
    [41, 12]
    ```



**List Methods**

- lists also have methods that can be used
- look up the full list using `x=list() >>> dir(x)`
  - `append` `count` `extend` `index` `insert` `pop` `remove` `reverse` `sort`



`append`

- we can create an empty list and then add elements using the `append` method
- the list stays in order and new elements are added at the end of the list



`in`

- python provides two operators that let you check if an item is in a list

- these are logical operators that return true or false

- they do not modify the list

- ```py
  >>> some = [1, 9, 21, 10, 16]
  >>> 9 in some
  True
  ```



**Order `sort`**

- a list can hold many items and keeps those items in the order until we do something to change the order
- a list can be sorted
- the `sort` method (unlike in strings) means "sort yourself"



**Other built in functions**

- `len(list)`
- `max(list)`
- `min(list)`
- `sum(list)`



**`split()`**

split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

- with no parameters it looks for 'spaces' (whitespaces including tabs)
- `split(';')` will split by the specified delimiter (semicolon).
- you can specify what delimiter character to use in the splitting



**Double split pattern**

- sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again



## FROM Textbook

The `*` operator on strings allows you to repeat a list a given number of times:

```py
>>> [0]*4
[0, 0, 0, 0,]
```



Since lists are mutable, it is often useful to make a copy before performing operations that fold, spindle or mutilate lists.

A slice operator on the left side of an assignment can update multiple elements:

```py
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
```



**List Methods**

Most list methods are void; they modify the list and return None. If you accidentally write `tsort = t.sort()`, you will be disappointed as t is assigned none.



**Lists and Strings**

A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. To convert from a string to a list of characters, you can use `list`

```py
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

If you want to break a string into words, you can use the `split` method.

`join` is the inverse of split. It takes a list of strings and concatenates the elements. `join` is a string method, so you have to invoke it on the delimiter and pass the list as a parameter.

```py
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

To concatenate strings without spaces, you can use the empty string `""`, as a delimiter 



