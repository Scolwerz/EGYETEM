#include<stdio.h>

int main()
{
    char c;

    printf("Adjon meg egy karaktert: ");
    scanf("%c", &c);

    if(c >= 'a' && c <= 'z')
    {
        printf("Kis betű\n");
    }

    else if(c >= 'A' && c <= 'Z')
    {
        printf("Nagy betű\n");
    }

    else if(c >= '0' && c <= '9')
    {
        printf("Szám\n");
    }

    else
    {
        printf("Egyéb karkater\n");
    }

    return 0;
}