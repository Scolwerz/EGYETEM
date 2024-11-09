#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 222

int main()
{
    char text[SIZE];
    int n=0, maxlength=-1;

    printf("Adj meg szavakat '*' vegjelig!\n");

    while (1)
    {
        printf("Szo: ");
        fgets(text, SIZE, stdin);
        int length = strlen(text);
        text[length-1] = '\0';

        if (strcmp(text, "*") == 0)
        {
            break;
        }
        else
        {
            if (length-1 > maxlength)
            {
                maxlength = length-1;
            }
            n++;
        }
    }
    puts("");

    printf("%d db szot adtal meg. A leghosszabb szo %d karakterbol all.", n, maxlength);

    return 0;
}