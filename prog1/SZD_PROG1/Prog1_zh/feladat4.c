#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 222

int main()
{
    char text[MAX];
    int count = 0;
    while (1)
    {
        printf("Az URL (vege: q): ");
        fgets(text, MAX, stdin);
        int length = strlen(text);
        text[length-1] = '\0';
        if (strcmp(text, "q") == 0)
        {
            break;
        }
        if (length > 8)   //Hiba length >= 8
        {
            text[8] = '\0';
            if (strcmp(text, "https://") == 0)
            {
                count++;
            }
        }
    }

    printf("\nHTTPS protokollt hasznalo URL-ek szama: %d", count);

    return 0;
}