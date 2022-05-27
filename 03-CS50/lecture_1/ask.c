////////////////////////////////////////////////////////////////////////////////
// Course: CS50 - Lecture 1
// Student: surge55
// Date: May 25, 2022
// Description: Practice code while following along to lecuture.
// Some code is commented as it is completed druing the lecture and replaced
// with new concepts. 
// <cs50.h> not downloaded during lecture and temporarily not available.
////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello, %s\n", answer);
}