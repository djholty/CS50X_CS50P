#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>



int main(void)
{
    string user_string = get_string("Please input your text to assess it's grade level: ");


    // initialize counters for letters, words, and sentences
    // printf("Your string is: %s\n", user_string);
    int x = strlen(user_string);
    // printf("Your string length is %i\n", x);
    int lettercounter = 0;
    int wordcounter = 1;
    int sentencecounter = 0;


// iterate through the string and count letters
    for (int i = 0; i < x ; i++)
    {

        if (isalpha(user_string[i]) != 0)
        {
            lettercounter ++;
        }
    }
    //printf("The number of letters is: %i\n", lettercounter);


//iterate through the string looking for spaces + 1 to find the number of words
    for (int i = 0; i < x ; i++)
    {

        if (isspace(user_string[i]) != 0)
        {
            wordcounter ++;
        }
    }


    //iterate through the string and find the number of sentences by looking for ., !, ?
    for (int i = 0; i < x ; i++)
    {

        if (user_string[i] == '.' || user_string[i] == '!' || user_string[i] == '?')
        {
            sentencecounter += 1;
        }
    }
    //printf("The number of sentences is: %i\n", sentencecounter);

// calculate the components of the coleman liau index and cast to float to avoid integer rounding errors
    float L = ((float) lettercounter / (float) wordcounter) * 100;
//printf("L is equal to %f\n", L);
    float S = ((float) sentencecounter / (float) wordcounter) * 100;
//printf ("F is equal to %f\n", S);
    float index = (.0588 * L) - (.296 * S) - 15.8;
    int rounded_index = round(index);
//printf("The index is: %i", rounded_index);


// output grade level based on the rounded index to the nearest grade level
    if (rounded_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rounded_index == 1)
    {
        printf("Grade 1\n");
    }
    else if (rounded_index == 2)
    {
        printf("Grade 2\n");
    }
    else if (rounded_index == 3)
    {
        printf("Grade 3\n");
    }
    else if (rounded_index == 4)
    {
        printf("Grade 4\n");
    }
    else if (rounded_index == 5)
    {
        printf("Grade 5\n");
    }
    else if (rounded_index == 6)
    {
        printf("Grade 6\n");
    }
    else if (rounded_index == 7)
    {
        printf("Grade 7\n");
    }
    else if (rounded_index == 8)
    {
        printf("Grade 8\n");
    }
    else if (rounded_index == 9)
    {
        printf("Grade 9\n");
    }
    else if (rounded_index == 10)
    {
        printf("Grade 10\n");
    }
    else if (rounded_index == 11)
    {
        printf("Grade 11\n");
    }
    else if (rounded_index == 12)
    {
        printf("Grade 12\n");
    }
    else if (rounded_index == 13)
    {
        printf("Grade 13\n");
    }
    else if (rounded_index == 14)
    {
        printf("Grade 14\n");
    }
    else if (rounded_index == 15)
    {
        printf("Grade 15\n");
    }
    else if (rounded_index == 16)
    {
        printf("Grade 16\n");
    }
    else if (rounded_index > 16)
    {
        printf("Grade 16+\n");
    }

}
// Coleman-Liau index index = 0.0588 * L - 0.296 * S - 15.8
// L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

//Function for counting Words ie. anyhting separated by a space

// Function for counting letters but shouldn’t include any punctuation, digits, or other symbols

//Function for counting sentences (anything ending in a . ! or ?)