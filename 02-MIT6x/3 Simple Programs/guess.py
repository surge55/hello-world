################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 16, 2022
## Exercise: guess my number
## In this problem, you'll create a program that guesses a secret number!
## The program works as follows: you (the user) thinks of an integer between 0
## (inclusive) and 100 (no inclusive). The computer makes guesses, and you give
## it input - is its guess too high or too low? Using bisection search, the 
## computer will guess the user's secret number!
##
## Note: your program should use `input` to obtain the user's input! Be sure to
## handle the case when the user's input is not one of `h`, `l`, or `c`
##
## When the user enters something invalid, you should print out a message to the
## user explaining you did not understand their input. Then, you should re-ask
## the question, and prompt again for input.
################################################################################

print("Please think of an number between 0 and 100!")

low = 0.0
high = 100
guess = int((low + high)/2)

while True:
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if response == 'c':
        break
    elif response == 'h':
        high = guess
        guess = int((low + high) / 2)
    elif response == 'l':
        low = guess
        guess = int((low + high) / 2)
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was:", guess)