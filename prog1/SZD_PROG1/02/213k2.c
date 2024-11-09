#include <stdio.h>

int main ()
{
    int x=0;
    
    while (x<=0)
    {
        printf("Adj meg egy pozitiv egeszet: ");
        scanf("%d", &x);
    }
    
    printf("A megadott pozitiv szam: %d\n", x);

    return 0;
}