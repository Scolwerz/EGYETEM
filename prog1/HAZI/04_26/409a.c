#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
    if (argc == 1)
    {
        fprintf(stderr, "Nem adtal meg egyetlen szot sem!");
        exit(1);
    }


    int min = strlen(argv[1]);
    for (int i=2; i<argc; i++)
    {
        int length = strlen(argv[i]);
        if (length < min)
        {
            min = length;
        }
    }

    for (int i=1; i<argc; i++)
    {
        if (strlen(argv[i]) == min)
        {
            printf("%s\n", argv[i]);
        }
    }
    
    return 0;
}