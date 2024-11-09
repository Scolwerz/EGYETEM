#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 222

int is_valid_c_identifier(const char* input)
{
    int length = strlen(input);
    
    //minimum 1 karakter
    if (length < 1)
    {
        return 0;
    }
    
    //első karakter jó-e
    if ((isupper(input[0]) || islower(input[0]) || input[0] == '_') == 0)
    {
        return 0;
    }
    
    //többi karakter jó-e
    for (int i=0; i<length; i++)
    {
        char current = input[i];
        if ((isupper(current) || islower(current) || isdigit(current) || current == '_') == 0)
        {
            return 0;
        }
    }
    
    return 1;
}

int main()
{
    char text[MAX];
    
    
    printf("Adj meg sztringeket '*' vegjelig!");
    while (1)
    {
        
        printf("\n\nInput: ");
        fgets(text, MAX, stdin);
        int length = strlen(text);
        text[length-1] = '\0';

        if (strcmp(text, "*") == 0)
        {
            break;
        }

        if (is_valid_c_identifier(text) == 1)
        {
            printf("YES");
        }
        else
        {
            printf("NO");
        }
    }
    
   
    
    return 0;
}