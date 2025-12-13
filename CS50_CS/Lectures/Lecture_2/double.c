#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size=get_int("Enter a size: ");
    int sequence[size];
    sequence[0]=1;
    printf("%i\n",sequence[0]);
    for (int i=0;i<(size-1);i++)
    {
        sequence[i+1]=sequence[i]*2;
        printf("%i\n",sequence[i+1]);
    }
}
