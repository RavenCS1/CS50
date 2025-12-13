#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;
int main(int argc, char* argv[])
{
    if (argc<1 || argc>=2)
    {
        printf("Usage ./pdf filename\n");
        return 1;
    }
    char* filename=argv[1];
    FILE *f = fopen(filename,"r");
    if (f==NULL)
    {
        return 2;
    }
    BYTE buffer[4];
    int blocks_read=fread(buffer,1,4,f);
    for (int i=0;i<4;i++)
    {
        printf("%i\n",buffer[i]);
    }
    printf("Blocks read: %i\n",blocks_read);
    fclose(f);
}
