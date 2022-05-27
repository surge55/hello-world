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

float discount(float price, int percentage)


int main(void)
{
    float regular = get_float("Regular price: ");
    int percent_off = get_int("Percent Off: ");
    float sale = discount(regular, percent_off); //regular * 0.85;
    printf("Sale Price: $%.2f\n", sale);
}

float discount(float price, int percentage)
{
    return price * (100 - percentage)/100;
}
