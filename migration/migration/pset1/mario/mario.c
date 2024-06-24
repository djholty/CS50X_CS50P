#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Please enter the height of the pyramid between one to eight: ");
    }
    while (height < 1 || height > 8);

    int level = 0;
    int j;
    int k = 0;
//iterate through the levels of the pyramid
    for (level = 0 ; level < height ; level++)
    {
        int spaces = height - (level + 1); //equation relating number of spaces to height of pyramid and current level
        //print the right number of spaces at the current level
        for (j = 0; j < spaces; j++)
        {
            //print spaces
            printf(" ");
        }
        //print the right number of hashes at the current level
        int hashes = level + 1; //equation relating number of hashes to current level
        for (k = 0; k < hashes ; k++)
        {
            printf("#");
        }

        printf("\n"); //move to next level
    }
}