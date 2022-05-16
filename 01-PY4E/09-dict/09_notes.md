__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 9 Notes 
## Dictionaries


__From Lecture__


Dictionaries are a useful construct, because it allows to have a mini database within python without having to connect a full on database.

List

- a linear collection of values that stay in order (e.g. Pringles can)

Dictionaries

- a "bag" of values, each with its own label (e.g. label or key to find what you are looking for)



**Dictionaries**

- Dictionaries are python's most powerful data collection
- Dictionaries allow us to do fast database-like operations in Python
- Dictionaries have different names in different languages:
  - Associative arrays - pear/php
  - Properties or Map or HashMap - Java
  - Property Bag - C# / .Net
- Lists index their entries based on the position in the list
- Dictionaries are like bags - no order
- So we index the things we put in the dictionary with a "lookup tag"



Dictionaries are like lists except that they use keys instead of numbers to look up values. Lists the key is a position value starting at 0. Dictionaries the key is a string that is user defined.

Are created using curly braces `{}` and keys and values separated by `:`



### Dictionary Use Cases 

One common use of dictionaries is counting how often we 'see' something

**Dictionary Tracebacks**

- It is an error to reference a key which is not in the dictionary
- We can use the `in` operator to see if a key is in the dictionary

**Histogram**

```py
counts = dict()
names 
```



**`get` Method**

- the pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us.
- Default value if key does not exist (and no traceback)



**Simplified counting with`get()`**

```py
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	counts[name] = counts.get(name, 0) + 1
print(counts)
```



## From Textbook



A **dictionary** is like a list, but more general. In a list, the index positions have to be integers, in a dictionary, the indices can be (almost) any type. Key-value pairs combined are an item.

The function `dict()` creates a new dictionary with no items. Because `dict` is the name of a built-in function, you should avoid using it as a variable name.

`{}` curly braces represent an empty dictionary.

In general, the order of items in a dictionary is unpredictable.



The `in` operator works on dictionaries, it tells you whether something appears as a key in the dictionary (appearing as a value is not good enough).

To see whether something appears as a value in a dictionary, you can use the method `values`, which returns the values as a *type* that can be converted to a list, and then use the `in` operator.

```py
>>> vals = list(eng2sp.values())
>>> 'uno' in vals
True
```



The `in` operator uses different algorithms for lists and dictionaries. For lists, it uses linear search algorithm. As the list gets longer, the search time gets longer in direct proportion to the length of the list. For dictionaries, Python uses an algorithm called a has table that has a remarkable property: the `in` operator takes about the same time no matter how many items there are in a dictionary. I 



An ***implementation*** is a way of performing a computation; some implementations are better than others.



Part of learning python is realizing that Python often has built-in capabilities for many common data analysis problems. Over time, you will see enough example code and read enough of the documentation to know where to look to see if someone has already written something that makes your job much easier.

`line = line.translate(line.maketrans('', '' , string.punctuation))`

Such as the above line that removes all punctuation from each line using the translate function.



### Debugging

As you work with bigger datasets it can become unwieldy to debug by printing and checking data by hand. Here are some suggestions for debugging large datasets:

- **Scale down the input**: If possible reduce the size of the dataset. Then slowly increase the size as you test and correct your code.

- **Check summaries and types**: Instead of printing and checking the entire dataset, consider printing summaries of the data.

- **Write self-checks**: sometimes you can write code to check for errors automatically. Detect results that are completely illogical.

- **Pretty print the output**: formatting debugging output can make it easier to spot and error

- Time you spend building scaffolding can reduce the time you spend debugging

  