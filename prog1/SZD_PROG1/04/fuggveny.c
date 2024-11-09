#include <stdio.h>
#include <stdlib.h>


int duplaz(int x)
{
    return 2*x;
}


int myabs(int x)
{
    if (x<0)
        return -x;
    return x;
}


int get_int()
{
    int x;
    printf("Adj meg egy egesz szamot: ");
    scanf("%d", &x);
    return x;
}


int get_p_int()
{
    int x;
    do
    {
        printf("Adj meg egy pozotiv egesz szamot: ");
        scanf("%d", &x);
    }
    while (x<=0);
    return x;
}


int get_p_int_2()
{
    int x;
    while (1)
    {
        printf("Adj meg egy pozotiv egesz szamot: ");
        scanf("%d", &x);
        if (x>0) break;
    }

}

int main()
{
    int result, x;
    // result = duplaz(x);

    // x = -4;
    // result = abs(x);
    // result = myabs(x);
    // printf("%d -> %d\n", x, result);

    // x = get_int();
    // printf("A megadott szam: %d\n", x);

    // x = get_positive_int();
    x = get_positive_int_2();
    printf("A megadott pozitiv szam: %d\n", x);


    return 0;
}