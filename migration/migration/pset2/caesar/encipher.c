#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc == 2) // check to make sure that there are only two arguments
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
            //iterate through the second argument looking to make sure each character is a digit
        {
            if (isdigit(argv[1][i]) == 0) // if this is equal to 0 then it is not a digit
            {
                printf("Usage: ./caesar key\n");  //if second argument is not a digit return and give error message
                return 1;
            }

        }

    }
    else // if there are not two arguments show error message and return
    {
        printf("Usage: ./caesar key Two arguments and the second one is an integer\n");
        return 1;
    }



    int key = atoi(argv[1]);  // turn second argument from string to int from stdlib.h
    string plaintext = get_string("plaintext: ");  //get plaintext message that will be converted using cypher key
    printf("ciphertext: ");



    for (int i = 0, n = strlen(plaintext); i < n; i += 1)
    {
        if isupper(plaintext[i]) //uppercase A = 65 in ascii decimal
        {
            char temp = plaintext[i] - 65;
            temp = (temp + key) % 26;
            temp = temp + 65;
            printf("%c", temp);
        }
        else if islower(plaintext[i]) //lowercase a = 97 in ascii decimal
        {
            char temp = plaintext[i] - 97; //subtract 97 to get the letter value between 0-25 inclusive
            temp = (temp + key) % 26; //run modulus operator to wrap numbers around appropriately
            temp = temp + 97; // add back 97 to get to the ascii letters
            printf("%c", temp);
        }
        else // if the character is not upper or lowercase then just print it as is
        {
            printf("%c", plaintext[i]);
        }

    }
    printf("\n");


}