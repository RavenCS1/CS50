#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1];
    int keylen = strlen(key);
    if (keylen != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0; i < keylen; i++)
    {
        if (isalpha(key[i]) == 0)
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
    }
    for (int i = 0; i < keylen - 1; i++)
    {
        for (int j = i + 1; j < keylen; j++)
        {
            if (key[i] == key[j] || key[i] == key[j] + 32)
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }
    string text = get_string("plaintext: ");
    int textlen = strlen(text);
    for (int i = 0; i < textlen; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            if (isupper(text[i]) != 0)
            {
                text[i] = toupper(key[text[i] - 65]);
            }
            else
                text[i] = tolower(key[text[i] - 97]);
        }
    }
    printf("ciphertext: %s\n", text);
    return 0;
}
