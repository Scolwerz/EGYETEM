#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 222

int jelszo(int n, char s[])
{
    int kb=0, nb=0, sz=0;
    if (n < 8)
    {
        return 0;
    }
    for (int i=0; i<n; i++)
    {
        if (s[i] >= '0' && s[i] <= '9')  sz=1;
        if (s[i] >= 'A' && s[i] <= 'Z')  nb=1;
        if (s[i] >= 'a' && s[i] <= 'z')  kb=1;
    }
    if (kb == 1 && nb == 1 && sz == 1)
    {
        return 1;
    }
    return 0;
}

int main()
{
    char text[SIZE];
    printf("Adj meg jelszavakat '*' vegjelig!\n");
    while (1)
    {
        printf("\nJelszo: ");
        fgets(text, SIZE, stdin);
        int length = strlen(text);
        text[length-1] = '\0';
        if (strcmp(text, "*") == 0)
        {
            break;
        }
        if (jelszo(length, text))
        {
            printf("eros jelszo\n");
        }
        else
        {
            printf("gyenge jelszo\n");
        }
    }
    
    return 0;
}