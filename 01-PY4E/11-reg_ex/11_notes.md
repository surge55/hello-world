__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 11 Notes
## Regular Expressions

*You don't have to program using regular expressions if you don't want to.*


In computing, a **regular expression**, also referred to as "regex" or "regexp", provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression is written in a formal language that can be interpreted by a regular expression processor.



Really clever "wild card" expressions, or really smart "Find" or "Search"

- Very powerful and quite cryptic
- Fun once you understand them
- Regular expressions are a language unto themselves
- A language of "marker characters" - programming with characters
- It is kind of an "old school" language - compact (1960s)



The Regular Expression

- Must import the library first `import re`
- You can use `re.search()` to see if a string matches a regular expression, similar to using the `find()` method for strings.
- You can use `re.findall()` to extract portions of a string that match your regular expression, similar to a combination of `find()` and slicing: `var[5:10]`

 

### Matching and Extracting

- `re.search()` returns a True/False depending on whether the string matches the regular expression
- If we actually want the matching strings to be extracted, we use `re.findall()`

```python
>>> import re
>>> x = "My 2 favourite numbers are 19 and 43"
>>> y = re.findall('[0-9]+', x)
>>> print(y)
['2', '19', '42']
```



-------------

From Textbook

---------------



We have been using string methods like `split` and `find` and using lists and string slicing to extract portions of lines.

This task of searching and extracting is so common the Python has a very powerful library called ***regular expressions*** that handle many of these tasks.

Regular expressions are almost their own little programming language for searching and parsing strings. Entire books have been written just on regular expressions.

The regular expression library `re` must be imported into your program before you can use it.

### Common Expressions

`^` - matches where lines <u>starts with</u>

`.` - matches any character (e.g. `F..M` would match any 4 character that starts with F and ends with M)



#### Examples

Search for lines that start with 'F', followed by 2 characters, followed by 'm':

```py
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^F..m', line):
		print(line)
```

....

Missed unsaved work FML

....

