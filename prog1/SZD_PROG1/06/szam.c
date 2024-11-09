#include <stdio.h>
#include "prog1.h"

int get_int(string s)
{
    printf("%s", s);
    int x;
    scanf("%d", &x);
    return x;
    
}

int main()
{
    int x = get_int("Adj meg egy számot: ");
    printf("A megadott szám %d\n", x);

    return 0;
}