################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge55
## Date: June 16, 2022
## Exercise: for
## In this problem you'll be given a chance to practice writing some for loops.
################################################################################

# 1. Convert the following code into code that uses a for loop
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!
print("EXERCISE 1:")
for i in range(2, 12, 2):
    print(i)
print('Goodbye!')


# 2. Convert the following code into code that uses a for loop
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
print("EXERCISE 2:")
print('Hello!')
for i in range(10, 0, -2):
    print(i)


# 3. Write a for loop that sums the values 1 through `end`, inclusive. `end` is a variable that we define for you.
#    So, for example, if we define `end` to be 6, your code should print the result (21). Which is 1 + 2 + 3 + 4 + 5 + 6
#    DO NOT USE a variable called `sum`
print("EXERCISE 3:")
end = 6
total = 0
for n in range(end+1):
    total += n
print(total)