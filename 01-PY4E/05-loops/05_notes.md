__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance

# Chapter 5 - Notes
## Iteration (and loops)


**In-Definite Loops** - Loops that could go on indefinitely. 

**Definite Loops** - Have a finite list of iterations or items to go through. "definite loops iterate through the members of a set"



### NoneType 

NoneType is the type for the `None` object, which is an object that indicates no value. None is used to indicate emptiness (not Null).



### Finding the Smallest Value

```python
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
	    smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
    
```



### The `is` and `is not` Operators

There's a subtle difference between the Python identity operator (is) and the equality operator (==). The == operator compares the value or equality of two objects, where the `is` operator checks whether two variables point to the same object in memory.

Use typically for None and Boolean check values



