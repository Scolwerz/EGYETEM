#include <stdio.h>
#include <stdlib.h>
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

int main ()
{
    char* text1 = "anna";
    char* text2 = "aNnA";
    char* text3 = "";
    char* text4 = "a";

    char* _text;
    _text = capitalise(text1); printf("%s --> %s\n", text1, _text); free(_text);
    _text = capitalise(text2); printf("%s --> %s\n", text2, _text); free(_text);
    _text = capitalise(text3); printf("%s --> %s\n", text3, _text); free(_text);
    _text = capitalise(text4); printf("%s --> %s\n", text4, _text); free(_text);

    return 0;
}