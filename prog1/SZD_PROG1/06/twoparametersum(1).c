#include <stdio.h>
#include "prog1.h"
#include <stdlib.h>

int main(int argc, string argv[])
{
    if(argc != 3)
    {
        printf("Hiba! Két paramétert (számot) kell megadni.\n");
        exit(1);
    }
    
    printf("%d\n", atoi(argv[1]) + atoi(argv[2]));

    return 0;
}