#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while ((height < 1) || (height > 8));
    //get the height and ensure it is between 1 - 8 inclusive
    //use the height to create a nested for loop to iterate down the rows of the pyramid and print out
    //appropriate spaces and hashes
    for (int i = 0; i < height; i++)
    {
        int spaces = height - i - 1;
        for (int j = 0; j < spaces; spaces--)
        {
            printf(" ");
        }

        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}