#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main()
{
    char sor[] = {".aa...,,.,,bbb.,.,.,,cc,,.,....,d,.,"};
    char* p;

/*  p = strtok(sor, " ");
    printf("'%s' ", p);
    p = strtok(NULL, " ");
    printf("'%s' ", p);
    p = strtok(NULL, " ");
    printf("'%s' ", p);
    p = strtok(NULL, " ");
    printf("'%s' ", p);
    p = strtok(NULL, " ");
    printf("'%p' ", p);  */

    p = strtok(sor, ".,");
    while (p != NULL)
    {
        printf("'%s'  ", p);
        p = strtok(NULL, ",.");
    }

    return 0;
}