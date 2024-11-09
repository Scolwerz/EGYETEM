#include <stdio.h>
#include <stdlib.h>
#include "string_utils.h"

int main()
{
    char* text1 = "aNnA";
    char text2[] = "asSgJSdg";
    char text3[] = lowercase(text2);
    char text4[] = uppercase(text2);
    printf("%s --> %s\n", text1, capitalise(text1));
    printf("%s --> %s\n", text2, text3);
    printf("%s --> %s\n", text2, text4);

    return 0;
}