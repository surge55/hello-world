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
    const int mine = 2;
    int points = get_int("How many did you lose?");

    if (points < mine) 
    {
        printf("You lost fewer points than me.\n");
    }
    else if (points > 2)
    {
        printf("You lost more points than me.\n");
    }
    else
    {
        printf("You lost the same amount of points as me.\n");
    }
}