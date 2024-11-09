#include <stdio.h>
#include <string.h>
#include "prog1.h"

#define MAX 26+1
void char_fillup(const int n, char t[])
{
    int i = 0;
    for (i=0; i<n; i++)
    {
        t[i]='a'+i;
    }
    t[i+1]='\0';
}

int main()
{
    char betuk[MAX];
    int meret = MAX;

    char_fillup(meret, betuk);
    printf("%s", betuk);

    return 0;
}