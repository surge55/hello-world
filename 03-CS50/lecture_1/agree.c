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
    // Prompt user to agree to something
    char c = get_char("Do you agree? ");

    // Check whether user agreed
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed\n");
    } 
    else if (c == 'n'|| c == 'N')
    {
        printf("Not Agreed\n");
    }
}