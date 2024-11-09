#include <stdio.h>
#include <string.h>
#include "prog1.h"

int rfind_char(string s, char c)
{
    for (int i=strlen(s); i>0; i--)
    {
        if (s[i] == c)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    printf("%d\n", rfind_char("Aladar", 'a'));

    return 0;
}