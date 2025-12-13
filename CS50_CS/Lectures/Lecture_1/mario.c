#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt user for pisitive integer
    int n;
    do
    {
       n=get_int("Size: ");
    }
    while (n<1);
    // Print an n-by-n grid of bricks
    for (int j=0; j<n;j++)
    {
        for(int i=0; i<n;i++)
        {
            printf("#");
        }
        printf("\n");
    }
}
