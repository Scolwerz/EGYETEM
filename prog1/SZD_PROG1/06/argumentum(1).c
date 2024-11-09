#include<stdio.h>
#include "prog1.h"

int main(int argc, string argv[])
{
    if(argc == 1)
    {
        puts("Hello World");
    }

    else if(argc == 2)
    {
        printf("Hello %s!\n", argv[1]);
    }
    
    else
    {
        puts("Túl sok parameter");
    }
    
    return 0;
}