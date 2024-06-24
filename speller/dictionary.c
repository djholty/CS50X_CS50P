// Implements a dictionary's functionality
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 35937;

// Hash table
node *table[N];

// declare global variables
int dictsize = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //convert word to lowercase so that it can be properly compared with dictionary words
    char tempword[strlen(word) + 1];  //declare new tempword array that will store lowercase version
    for (int i = 0, n = strlen(word) + 1; i < n; i++)
    {
        tempword[i] = tolower(word[i]);
    }
    //printf("Lowercase word: %s\tWord: %s\n", tempword, word );
    // pass lowercase word through the hash to get back the correct bucket number so that you are doing a proper comparison
    // with two lowercase words
    int hashnumber = hash(tempword);
    //printf("Hashnumber: %i\n",hashnumber);

    // run through the link list comparing the words in the nodes to this new tempword
    node *ptr = table[hashnumber]; // create variable ptr to traverse the linked list starting at the hashtable head
    //printf("Hashtable Head word: %s\n", ptr->word);
    while (ptr != NULL)
    {
        if (strcasecmp(tempword, ptr->word) == 0)
        {
            //printf("Found in Dictionary");
            return true;
        }
        // printf("Dictionary words: %s\n", ptr->word);
        ptr = ptr->next;

    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //from https://www.strchr.com/hash_functions
    // Bernsteins function uses hashval as 5381 and 33 as multiplier
    // Kernighan and Ritchie's function is 0 and 31
    // a multiplicative hash function
    char tempword[strlen(word) + 1];
    //convert word into lowercase version for hashing
    for (int i = 0, n = strlen(word) + 1; i < n; i++)
    {
        tempword[i] = tolower(word[i]);
    }

    unsigned int hashval = 5381;
    for (int i = 0; i < strlen(tempword); i++)
    {
        hashval = 31 * hashval + tempword[i];
    }
    //printf("%i\n", hashval%N);

    return hashval % N;
}



// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }
    char buffer; // declare character buffer
    char dictword[LENGTH + 1]; // declare word array to store word
    int index = 0; //declare index variable
    //set all values of hash table to NULL initially
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    while (fread(&buffer, sizeof(char), 1, dict) > 0)
    {
        if (buffer != '\n')
        {
            dictword[index] = buffer;
            index++;
        }
        else if (buffer == '\n') //end of word
        {
            dictword[index] = '\0';
            //printf("%s\n", dictword);
            index = 0; //reset index to 0 for new word
            //store word in a new node
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                printf("No available memory for new node");
                return false;
            }
            //copy word into the node
            strcpy(n->word, dictword);
            //printf("Loaded %s into dictionary\n", n->word);
            //assign the next variable to NULL
            n->next = NULL;


            //get hashnumber by passing word through hash function
            int hashnumber = hash(dictword);

            //if this is the first item in the list then assign the array hashnumber, the address of the first node
            if (table[hashnumber] == NULL)
            {
                table[hashnumber] = n;
                dictsize++;
            }
            else // assign the next value to the head of the list, then reassign the head to the new node (adds node at beginning)
            {
                n->next = table[hashnumber];
                table[hashnumber] = n;
                dictsize++;
            }
        }

    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dictsize;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{

    // Free memory
    //iterate through the hashtable one by one and then free the linked list associated with each hash table entry
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];  //make ptr point to the head of the table
        while (ptr != NULL)
        {
            node *next = ptr->next;  //point ptr to the next node in the linked list
            free(ptr);  //free current pointer
            ptr = next;  //reassign ptr to the next node
        }
        if (ptr == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
