#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "prog1.h"

int main(int argc, string argv[])
{
    if (argc > 2)
    {
        printf("Hiba! Maximum egy paraméter adható meg!\n");
        exit(1);
    }
    
    if (argc == 1)
    {
        printf("Hello World!\n");
        exit(0);
    }
    string nev = argv[1];
    if (strcmp(nev, "Batman") == 0 || strcmp(nev, "Robin") == 0) 
    {
        printf("Denevérveszély!\n");
        exit(0);
    }
    printf("Hello %s!\n", argv[1]);

    return 0;
}