// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int count;
unsigned int bucket;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    bucket = hash(word);
    node* cursor = table[bucket];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long sum = 0;
    for (int i = 0, len = strlen(word); i<len; i++)
    {
        sum += toupper(word[0]);
    }
    sum = sum % N;
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open %s\n", dictionary);
        return false;
    }
    char string[LENGTH+1];
    while (fscanf(source, "%s", string) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
            return false;
        strcpy(n->word, string);
        bucket = hash(string);
        n->next = table[bucket];
        table[bucket] = n;
        count++;
    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (count > 0)
        return count;
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        if (cursor == NULL && i == N-1)
            return true;
    }
    return false;
}
