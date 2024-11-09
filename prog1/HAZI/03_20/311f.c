#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

int char_count(string s, char c)
{
    int n = strlen(s);
    int count = 0;
    for (int i=0; i<n; i++)
    {
        if (s[i] == c)
        {
            count++;
        }
    }
    return count;
}

int main()
{
    printf("%d\n", char_count("Abba", 'b'));
    printf("%d\n", char_count("Abba", 'a'));
    printf("%d\n", char_count("Abba", 'x'));
    
    return 0;
}
