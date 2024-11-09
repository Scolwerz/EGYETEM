#include <stdio.h>
#include <stdlib.h>
#include "prog1.h"


int main(int argc, string argv[])
{
    if (argc != 3)
    {
        printf("Hiba! Ket parametert (szamot) kell megadni.\n");
        exit(1);
    }
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    
    printf("%d\n", a+b);
    
    return 0;
}