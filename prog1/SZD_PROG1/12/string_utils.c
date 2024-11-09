#include "string_utils.h"

#include <stdio.h>
#include <string.h>
#include <ctype.h>


char* capitalise(const char* text)
{
    int length = strlen(text);
    char* s = malloc(length * sizeof(char));
    s[0] = toupper(text[0]);
    for (int i = 1; i < length; i++)
    {
        s[i] = tolower((text[i]));
    }

    return s;
}

void lowercase(char s[])
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        s[i] = tolower(s[i]);
    }
}

void uppercase(char s[])
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        s[i] = toupper(s[i]);
    }
}