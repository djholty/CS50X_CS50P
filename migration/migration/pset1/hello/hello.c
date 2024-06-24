#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //get name and print it
    string name = get_string("Please enter your first name: ");
    printf("hello, %s\n", name);
}