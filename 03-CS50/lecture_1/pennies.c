#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main(void)
{
    float amount = get_float("Dollar amount: ");
    int pennies = round(amount * 100);     // round up to help with storing the imprecision value
    printf("Pennies: %i\n", pennies);
}