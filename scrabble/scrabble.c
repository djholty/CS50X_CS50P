#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int LOWERCASE[] = {97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122 };
int UPPERCASE[] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90};
//                 a   b   c   d,  e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!");
        //printf("Player 1 scored %i and player 2 scored %i\n", score1, score2);
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
        //printf("Player 2 scored %i and player 1 %i\n", score2, score1);
    }
    else
    {
        printf("It is a tie\n");
    }

}

int compute_score(string word)
{
    int totalscore = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int k, j;
        if (isupper(word[i]))
        {
            for (j = 0; j < 26; j++)
            {
                if (word[i] == UPPERCASE[j])
                {
                    totalscore = totalscore + POINTS[j];
                }
            }
        }
        if (islower(word[i]))
        {
            for (k = 0; k < 26; k++)
            {
                if (word[i] == LOWERCASE[k])
                {
                    totalscore = totalscore + POINTS[k];
                }
            }
        }
    }
    return totalscore;
}