__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 3 Notes
## Conditional Execution

A **Boolean expression** is an expression that is either true or false.

Remember that a single equal sign (`=`) is an assignment operator and (`==`) is a comparison operator.



There are three **logical operators**: `and`, `or` and `not`.

Python is not very strict. Any nonzero number is interpreted as "true", example:

```python
>>> 17 and True
True
```

This flexibility can be useful, but there are some subtleties to it that might be confusing. You might want to avoid it until you are sure you know what you are doing.



### 3.7 Catching Exceptions Using try and except

There is a conditional execution structure built into Python to handle expected and unexpected errors called **"try / except"**. The idea of `try` and `except` is that you know that some sequence of instruction(s) may have a problem and you want to add some statements to be executed if an error occurs. These extra statements (the except block) are ignored if there is no error.

We can rewrite our temperature converter as follows:

```python
inp = input("Enter Farenheit Temperature:")
try:
    fahr = float(inp)
    cel = (fahr -32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
```

Handling an exception with a try statement is called *catching* an exception. In general, catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.



### 3.8 Short-circuit evaluation of logical expressions

When Python is processing a logical expression, it evaluates it from left to right. In cases of the **and** logical operator, where the first part of the logical expression is False regardless of whether the second part of the expression evaluates to True or False, the expression would result in False.

When Python detects that there is nothing to be gained by evaluating the rest of a logical expression, it stops its evaluation and does not do the computations in the rest of the logical expression. When the evaluation of a logical expression stops because the overall value is already known, it is called **short-circuiting** the evaluation. 

While this may seem like a fine point, the short-circuit behavior leads to a clever technique called the **guardian pattern**. Consider the following code sequence in the Python interpreter.

```python
x = 6
y = 2
x >= 2 and (x/y) > 2
>>> True

x = 1
y = 0
x >= 2 and (x/y) > 2
>>> False

x = 6
y = 0
x >= 2 and (x/y) > 2
```

All three logical expressions are the *same*

The second calculation worked!

The third calculation failed - because the expression is dividing by zero. The first and second examples did not fail because the first part of these expressions `x >= 2` evaluated to False so the `(x/y)` was not ever executed due to the short-circuit rule and there was no error.

We can construct the logical expression to strategically place a guard evaluation just before the evaluation that might cause an error as follows:

```python
x = 1
y = 0
x >= 2 and y != 0 and (x/y) > 2
>>> False

x = 6
y = 0
x >= 2 and y != 0 and (x/y) > 2
>>> False

x >= 2 and (x/y) > 2 and y != 0
ZeroDivisionError: division by Zero
```

First logical expression, is False in the fist component (x >= 2) so the evaluation stops at the first `and`.

Second logical expression, is False in the second component (y != 0) so the evaluation stops at the second `and`, so we never reach (x/y).

Third logical expression, Fails with an error at the second component because it divides by zero.

In the **second expression**, we say that `1 != 0` acts as a ***guard*** to insure that we only execute `(x/y)` if `y` is non-zero.

