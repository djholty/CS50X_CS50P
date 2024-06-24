#include <stdio.h>
#include <cs50.h>

// function to get a name and write hello name
int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}