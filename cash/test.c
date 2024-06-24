#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s), j = 1, k = 20; i < n & j < n; i++, j++, k=k+2)
    {
        //printf("%c", toupper(s[i]));
        printf("%d%d",j,k);
        //printf("%d", k);
    }
    printf("\n");
}