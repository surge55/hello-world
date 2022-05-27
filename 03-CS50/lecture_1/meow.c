////////////////////////////////////////////////////////////////////////////////
// Course: CS50 - Lecture 1
// Student: surge55
// Date: May 25, 2022
// Description: Practice code while following along to lecuture.
// Some code is commented as it is completed druing the lecture and replaced
// with new concepts.
////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdbool.h> // Needed for while(true) condition on line 18

void meow(int n);

int main(void)
{
    // print forever
    // while (true)
    // {
    //     printf("Meow\n");
    // }

    // print 3 times, user i instead of counter
    printf("while loop\n");
    int i = 0;
    while (i < 3)
    {
        printf("Meow\n");
        i++;
    }

    // print 3 times, using for loop
    printf("for loop\n");
    for (int i = 0; i < 3; i++)
    {
        printf("Mmow\n");
    }

    // print 3 times, using custom function 'meow'
    // printf("for loop + meow function\n");
    // for (int i = 0; i < 3; i++)
    // {
    //     meow();
    // }
    printf("function(n)\n");
    meow(4);

}

void meow(int n)
{
    // meow n number of times
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}