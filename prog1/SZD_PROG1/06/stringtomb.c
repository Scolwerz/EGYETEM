#include <stdio.h>
#include "prog1.h"
#include <string.h>

int main()
{
    string szavak[3] = {"abc", "fgh", "zxyab"};
    int meret=3;

    for(int i=0; i<meret; ++i)
    {
        printf("%d\n", strlen(szavak[i]));
    }
    puts("");

    for(int i=0; i<meret; ++i)
    {
        for(int j=0; j<strlen(szavak[i]) ; ++j)
        {
        printf("%c\n", szavak[i][j]);
        }
    }
    
    return 0;
}