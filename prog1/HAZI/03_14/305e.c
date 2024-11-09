#include <stdio.h>
#include <stdlib.h>

int is_even(int x)
{
    if (x%2 == 0)
    {
        return 1;
    }
    return 0;
}

int is_odd(int x)
{
    if (is_even(x) == 1)
    {
        return 0;
    }
    return 1;
}


int main()
{
    int x;

    printf("Adj meg egy szamot [egesz]: ");
    scanf("%d ", &x);

    if (is_even(x) == 1)
    {
        printf("paros");
    }
    else
    {
        printf("paratlan");
    }
    printf("\n---------\n");
    if (is_odd(x) == 1)
    {
        printf("paratlan");
    }
    else
    {
        printf("paros");
    }
    
    return 0;
}