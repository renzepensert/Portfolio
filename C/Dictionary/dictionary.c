/*
 *  Implements a dictionary's functionality
 *  Rens Groot
 *  13122304
 */
#include <cs50.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"


// create struct node
typedef struct node
{
    char wordcopy[LENGTH + 1];
    struct node* next;
} node;

// global variables
int word_count = 0;

// create pointer hashtable
node *hashtable[26];

// returns true if word is in dictionary else false
bool check(const char *word)
{
    // takes the length of the word
    int word_length = strlen(word);

    // store the word
    char temp_word[word_length + 1];

    // sets the last character in this array to \0
    temp_word[word_length] = '\0';

    // make the word lowercase
    for (int i = 0; i < word_length; i++)
    {
        temp_word[i] = tolower(word[i]);
    }
    // hash the word
    unsigned long hashed = temp_word[0] - 97;

    // initialize head and let it point to the first element in linked list of the bucket
    node *head = hashtable[hashed];

    // if there is at least one element in the bucket
    if (head != NULL)
    {
        // initialize a pointer named cursor
        node* cursor = head;

        while(cursor != NULL)
        {
            // checks if words are the same
            if(strcmp(temp_word, cursor->wordcopy) == 0)
            {
                return true;
            }
            // moves to next element of linked list
            cursor = cursor->next;
        }
    }
    return false;
}

// loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // initialize load_word
    char load_word[LENGTH + 1];

    // reads input file and gives an error when the file can't be read
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", dictionary);
        return false;
    }
    // reads formatted input from a stream
    while (fscanf(inptr, "%s", load_word) == 1)
    {
        // allocate memory and create a pointer to it
        node *node_bucket_temp = malloc(sizeof(node));

        // if the pointer points to nothing because malloc cant allocate any memory
        if(node_bucket_temp == NULL)
        {
            fprintf(stderr, "Cant allocate memory for node \n");
        }
        node_bucket_temp->next = NULL;

        // copy loaded word to wordcopy
        strcpy(node_bucket_temp->wordcopy, load_word);

        // takes the length of the word
        int word_length = strlen(load_word);

        // store the word + null terminator
        char temp_word[word_length + 1];

        // sets the last character in this array to \0
        temp_word[word_length] = '\0';

        // hash the first letter of the loaded word
        unsigned long hashed = load_word[0] - 97;

        // initialisation pointer temp
        node* temp = NULL;

        // if the hashtable points to nothing yet
        if (hashtable[hashed] == NULL)
        {
            // point the hashtable to the newly created node
            hashtable[hashed] = node_bucket_temp;
        }

        // when there are already one or more nodes in a list the hashtable points to
        else
        {
            // let temp point to the node the hashtable points to
            temp = hashtable[hashed];

            // go through the linked list untill a node points to nothing (last element in linked list)
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            // last element in linked list points to the newly created node
            temp->next = node_bucket_temp;
        }
        // count the size of the wordlist
        word_count++;
    }
    // close the file
    fclose(inptr);

    return true;
}

// returns number of words in dictionary
unsigned int size(void)
{
    return word_count;
}

// unloads dictionary from memory
bool unload(void)
{
    // go through all 26 buckets
    for (int i = 0; i < 26; i++)
    {
        // initiate cursor and let it point to the first element in linked list in that bucket
        node *cursor = hashtable[i];

        // go through the whole linked list
        while (cursor != NULL)
        {
            node* tmp = cursor;
            cursor = cursor->next;

            // free the memory
            free(tmp);
        }
    }

    return true;
}
