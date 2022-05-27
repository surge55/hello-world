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
    // do while loop - checks the condiion last instead of first
    int n;
    do 
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    // for (int i = 0; i < n; i++)
    // {
    //     print("?");
    // }
    // printf("\n");

    // For each row
    for (int i = 0; i < n; i++)
    {    
        // For each column
        for (int j = 0; j < n; i++)
        {
            // make a brick
            printf("#");
        }   
            // move down a line
            printf("\n");
    }
}