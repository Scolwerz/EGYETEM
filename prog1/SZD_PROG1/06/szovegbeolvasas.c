#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1023
int main()
{
    char t[MAX];
    printf("Írj be egy szöveget: ");
    fgets(t, MAX, stdin);
    t[strlen(t)-1]='\0';
    printf("'%s'\n", t);

    return 0;

}