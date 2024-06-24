#include <cs50.h>
#include <stdio.h>


int main(void)
{
    //Prompt user for start size
    int startsize;
    do
    {
        startsize = get_int("Please enter the starting size of your population (must be at least 9): ");
    }
    while (startsize < 9);

    //Prompt user for end size

    int endsize;
    do
    {
        endsize = get_int("Please enter the ending size of your population: ");
    }
    while (endsize < startsize);

    //Calculation of number of years until we reach threshold lamas grow by n/3 and die by n/4 yearly
    //initialize i outside for loop for use outside of for loop afterwards.
    int newpop = startsize;
    int i;
    for (i = 0; endsize > newpop; i++)
    {
        newpop = newpop + (newpop / 3) - (newpop / 4);
    }

    //Print Number of years

    printf("Years: %i\n", i);
}