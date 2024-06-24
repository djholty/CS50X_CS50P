#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string s);

int main(int argc, string argv[])
{

    //printf("Usage: ./caesar key\n");  //if second argument is not a digit return and give error message
    if (argc != 2) // check to make sure that there are only two arguments
    {
        printf("Usage: ./caesar key\n");
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


bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++) //iterate through the string looking to make sure each character is a digit
    {
            if (isdigit(s[i]) == 0) // if isdigit(s[i]) is equal to 0 then it is not a digit
            {

                return false;
            }

    }
    return true;
}