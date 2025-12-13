#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    int width = 1;
    int spaces = height - width;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        spaces--;
        if (spaces == -1)
        {
            spaces = 0;
        }
        for (int k = 0; k < width; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int k = 0; k < width; k++)
        {
            printf("#");
        }
        printf("\n");
        width++;
    }
}
