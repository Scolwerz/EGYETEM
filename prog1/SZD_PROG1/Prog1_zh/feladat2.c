#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

#define MAX 222   //Hiba: MAX = 100

void uniq(string input, char output[])
{
    int length = strlen(input);
    int n = 0;

    for (int i = 0; i < length; i++)
    {
        int count = 0;
        for (int j = 0; j < length; j++)
        {
            if (input[i] == input[j])
            {
                count++;
            }
        }
        if (count == 1)
        {
            output[n] = input[i];
            n++;
        }
    }
    output[n] = '\0';
}

int main()
{
    char text[MAX];
    char result[MAX];

    printf("Input: ");
    fgets(text, MAX, stdin);
    int text_length = strlen(text);
    text[text_length-1] = '\0';

    uniq(text, result);
    printf("Output: %s", result);

    return 0;
}