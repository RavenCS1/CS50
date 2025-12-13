#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string phrase = get_string("Enter a phrase: ");
    for (int i = 0, n=strlen(phrase); i<(n-1) ;i++)
    {
        if (phrase[i]>phrase[i+1])
        {
            printf("Not in alphabetical order.\n");
            return 0;
        }
    }
    printf("Alphabetical order!\n");
}
