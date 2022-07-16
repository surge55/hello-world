////////////////////////////////////////////////////////////////////////////////
// Course: CS50 - Problem Set 1
// Student: surge55
// Date: May 26, 2022
// Description: Submit the less comfortable version of Mario, which prints the
// left side of the mario pyramid of height 1-8: Example Height = 8
//        #
//       ##
//      ###
//     ####
//    #####
//   ######
//  #######
// ########
// <cs50.h> not downloaded executed in cloud environment for submission
////////////////////////////////////////////////////////////////////////////////

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // do while loop - ask the user for a number between 1 and 8, inclusive
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);



    // Print Pyramid

    // For each ROW
    for (int i = 0; i < n; i++)
    {


        // For each COLUMN

        // Print BLANKS/DOT n times
        for (int j = n - i - 1; j > 0; j--) // j needs to decrement each time a new row (i) starts
        {
            printf(" ");
        }

        // Print HASHES n times
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        // move down a line
        printf("\n");
    }
}