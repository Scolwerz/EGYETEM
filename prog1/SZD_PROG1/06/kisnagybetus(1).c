#include <stdio.h>
#include "prog1.h"
#include <string.h>
#include <ctype.h>

char upper(const char c)
{
    if(c >= 'a' && c <= 'z')
    {
        return c - ('a'-'A');
    }
    else
    {
        return c;
    }
}

char lower(const char c)
{
    if(c >= 'A' && c <= 'Z')
    {
        return c + ('a'-'A');
    }
    else
    {
        return c;
    }
}

int main()
{
    string text = "hello";
    string text2 = "MerNOK";

    for (int i=0; i<strlen(text); ++i)
    {
        printf("%c", upper(text[i]));
    }
    puts("");

    for (int i=0; i<strlen(text2); ++i)
    {
        printf("%c", lower(text2[i]));
    }
    puts("");


    for (int i=0; i<strlen(text); ++i)
    {
        printf("%c", toupper(text[i]));
    }
    puts("");

    for (int i=0; i<strlen(text2); ++i)
    {
        printf("%c", tolower(text2[i]));
    }
    puts("");

    return 0;
}