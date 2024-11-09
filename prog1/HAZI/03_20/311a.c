#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

int match_ends(int n, string words[])
{
    int count = 0;
    for (int i=0; i<n; i++)
    {
        int length = strlen(words[i]);
        if (length > 1 && words[i][0] == words[i][length-1])
        {
            count++;
        }
    }
    return count;
}

int main()
{
    string szavak1[] = { "aba", "xyz", "aa", "x", "bbb" };
    string szavak2[] = { "", "x", "xy", "xyx", "xx" };
    string szavak3[] = { "aaa", "be", "abc", "hello" };
    int szavak1_meret = 5;
    int szavak2_meret = 5;
    int szavak3_meret = 4;

    for (int i=0; i<szavak1_meret; i++)
    {
        puts(szavak1[i]);
    }
    printf("%d\n\n", match_ends(szavak1_meret, szavak1));
    
    for (int i = 0; i < szavak2_meret; i++)
    {
        puts(szavak2[i]);
    }
    printf("%d\n\n", match_ends(szavak2_meret, szavak2));
    
    for (int i = 0; i < szavak3_meret; i++)
    {
        puts(szavak3[i]);;
    }
    printf("%d\n", match_ends(szavak3_meret, szavak3));
    
    return 0;
}
