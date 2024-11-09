#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

void filter(string s1, string s2)
{
    int length1 = strlen(s1);
    int length2 = strlen(s2);

    putchar('"');
    for (int i = 0; i < length1; i++)
    {
        for (int j = 0; j < length2; j++)
        {
            if (s1[i] == s2[j])
            {
                printf("%c", s1[i]);
                break;
            }
        }
    }
    putchar('"');
}

int main(int argc, string argv[])
{
    if (argc != 3)
    {
        printf("Hiba! Adj meg pontosan 2 db parametert!");
        exit(1);
    }

    filter(argv[1], argv[2]);

    return 0;
}