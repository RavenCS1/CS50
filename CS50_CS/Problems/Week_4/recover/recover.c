#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover filename\n");
        return 1;
    }
    FILE *src = fopen(argv[1], "r");
    if (src == NULL)
    {
        printf("File could not have been opened\n");
        return 1;
    }
    BYTE buffer[512];
    int found = 0;
    char filename[8];
    int counter = 0;
    FILE *new = NULL;
    while (fread(buffer, 1, sizeof(buffer), src) == sizeof(buffer))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            found++;
        }
        if (found == 1)
        {
            if (counter != 0)
            {
                fclose(new);
            }
            sprintf(filename, "%03i.jpg", counter);
            new = fopen(filename, "w");
            fwrite(buffer, 1, sizeof(buffer), new);
            found--;
            counter++;
        }
        else if (counter != 0)
        {
            fwrite(buffer, 1, sizeof(buffer), new);
        }
    }
    fclose(src);
    fclose(new);
}
