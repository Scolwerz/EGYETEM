#include <stdio.h>

int main ()
{
    int x;
    
    do
    {
        printf("Adj meg egy pozitiv egeszet: ");
        scanf("%d", &x);
        if (x<=0)
        {
            printf("-> ez nem pozitiv egesz\n\n");
        }
    }
    while (x<=0);
        
    printf("A megadott pozitiv szam: %d\n", x);

    return 0;
}