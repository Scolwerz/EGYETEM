#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 222

int main()
{
    char s[MAX];
    int sum = 0;
    int length;
    
    printf("Szam: ");
    fgets(s, MAX, stdin);
    length = strlen(s)-1;   
    for (int i=0; i<length; i++)
    {
        sum += s[i] - '0';
    }
    printf("\nA szamjegyek osszege: %d", sum);
    
    return 0;
}