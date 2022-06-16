################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge55
## Date: June 16, 2022
## Exercise: while
## In this problem you'll be given a chance to practice writing some while loops.
################################################################################

# 1. Convert the following code that uses a while loop
#  prints 2
#  prints 4
#  prints 6
#  prints 8
#  prints 10
#  prints Goodby!
print('EXERCISE 1:')
n = 2
while n <= 10:
    print(n)
    n += 2
print('Goodbye!')


# 2. Convert the following into code that uses a while loop.
#  prints Hello!
#  prints 10
#  prints 8
#  prints 6
#  prints 4
#  prints 2
print("EXERCISE 2:")
n = 10
print('Hello!')
while n > 0:
    print(n)
    n -= 2


# 3. Write a while loop that sums the values 1 through `end`, inclusive. `end` is a variable that we define for you.
#    So, for example, if we define `end` to be 6, your code should print out the result (21).
#    Which is 1 + 2 + 3 + 4 + 5 + 6
#    DO NOT USE a variable called `sum`
print("EXERCISE 3:")
end = 6
s = 0
total = 0
while s < end:
    s += 1
    total = total + s
print(total)