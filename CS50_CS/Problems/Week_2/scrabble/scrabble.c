#include <cs50.h>
#include <stdio.h>
#include <string.h>

int values[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int compute_score(string word);
int main(void)
{
    string answer1 = get_string("Player 1: ");
    string answer2 = get_string("Player 2: ");
    int score1 = compute_score(answer1);
    int score2 = compute_score(answer2);
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    int sum = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (word[i] >= 65 && word[i] <= 90)
        {
            sum += values[word[i] - 65];
        }
        else if (word[i] >= 97 && word[i] <= 122)
        {
            sum += values[word[i] - 97];
        }
    }
    return sum;
}
