#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

int rfind_char(string s, char c)
{
    int n = strlen(s)-1;
    for (int i=n; i>=0; i--)
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
    printf("%d\n", rfind_char("Abba", 'x')); 
    printf("%d\n", rfind_char("Abba", 'a'));
    printf("%d\n", rfind_char("Aladar", 'a'));
    printf("%d\n", rfind_char("Abba", 'b'));
   
   return 0;
}
