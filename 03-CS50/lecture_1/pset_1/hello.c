////////////////////////////////////////////////////////////////////////////////
// Course: CS50 - Problem Set 1
// Student: surge55
// Date: May 26, 2022
// Description: Submit Hello, which asks the user for their name and prints
// hello and the users name.
// <cs50.h> not downloaded executed in cloud environment for submission
////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Enter your name: ");
    printf("hello, %s\n", name);
}