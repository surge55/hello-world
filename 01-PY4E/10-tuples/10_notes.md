__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 10 Notes
## Tuples

Tuples are another kind of sequence that functions much like a list

- they have elements which are indexed starting at 0
- Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
  - This is to be more efficient and faster than lists

`x = (9, 8 ,7)`



**Things you CAN'T do with Tuples:**

- Cannot sort()
- Cannot append()
- Cannot revers()

**Things you CAN do with Tuples:**

- Count
- Index



**Tuples are more efficient:**

- Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory user and performance than lists
- So in our program when we are making "temporary variables" we prefer tuples over lists
-  We can also put a tuple on the left-hand side of an assignment statement (behaves like a double assignment)
- You can return tuples from functions
- We can even omit the parentheses

```py
>>> (x, y = (4, 'fred')
>>> print(y)
fred
>>> (a, b) = (99, 98)
>>> print(a)
99
```



**Tuples in Dictionaries**

You can loop through the key value pairs of the dictionary using a tuple.

```py 
>>> for (k,v) in d.items():
	print(k,v)
```



**Tuples are Comparable**

- The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element pair and so on until it finds elements that differ



### Sorting Lists of Tuples

- We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
- Sort always looks at the first item in a tuple to compare it
- First we sort the dictionary by the key using the items() method and sorted() function

```py
>>> d = {'a':10, 'b':1, 'c':22}
>>> d.items()
dict_items([('a', 10), ('c', 22), ('b': 1)])
>>> sorted(d.items())
[('a', 10), ('b', 1), ('c', 22)]
```

It compares the keys of the dictionary, it sorts by the Keys. Keys are always unique and distinct for a dictionary.

**Sort by Values instead of Key**

- If we could construct a list of tuples of the form (value, key) instead of *key,value* we could sort by value - FLIP the order of the pair
- We do this with a for loop that creates a list of tuples

```py
>>> for k, v in a_tuple.items():
...		tmp_list.append( (v,k) )
```



**Shorter version of the same code**

`print( sorted( [ (v,k) for k, v in c.items() ] ) )`

*List comprehension* creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.



### Which Sequence to Use?

In many contexts, the different kinds of sequences (strings, lists, and tuples) can be used interchangeably. So how and why do you choose one over the others?

**strings**

- obviously has to be a sequence of characters
- are immutable
- are hashable
- if you need the ability to change the characters in a string (as opposed to creating a new string), you might want to use a list of characters instead.

**lists**

- are more common than tuples
- are mutable
- are not hashable

**tuples**

- In some contexts, like a *return* statement it is syntactically simpler to create a tuple than a list.
- If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or a string
- If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behaviour due to aliasing
- Because tuples are immutable, they don't provide methods like sort and reverse, which modify existing lists. However Python provides the built-in functions sorted and reversed, which take any sequence as a parameter and return a new sequence with the same elements in a different order.



### Debugging

Lists, dictionaries and tuples are known generically as data structures; in this chapter we are starting to see compound data structures, like lists of tuples, and dictionaries that contain tuples as keys and lists as values.

Compound data structures are useful, but they are prone to what I call shape errors; that is, errors caused when a data structure has the wrong type, size or composition, or perhaps you write some code and forget the shape of your data and introduce an error. For example, if  you are expecting a list with one integer and I give you a plain old integer (not in a list), it won't work.