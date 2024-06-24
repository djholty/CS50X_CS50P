#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //Get a positive amount of change as input
    int coincount = 0;
    float f;
    do
    {
        f = get_float("Please input the total amount of change and we will tell you the least number of coins you will receive in return: $");
    }
    while (f < 0);

int cents = round(f*100);

//go through the change amount subtracting quarters until you cant take out any more quarters

    while (cents >= 25)
    {
        cents = cents - 25;
        coincount = coincount + 1;

    }
//subtract out dimes until you cant get anymore dimes
    while (cents >= 10)
    {
        cents = cents - 10;
        coincount = coincount + 1;

    }
//subtract out nickels
    while (cents >= 5)
    {
        cents = cents - 5;
        coincount = coincount + 1;
    }
//subtract out pennies
    while (cents >= 1)
    {
        cents = cents -1;
        coincount = coincount + 1;
    }

    printf("You have received %i coins as change\n", coincount);
}