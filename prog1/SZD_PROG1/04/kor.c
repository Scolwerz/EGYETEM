#include <stdio.h>
#include <math.h>

double kerulet(int r)
{
    return 2*r*3.14;
}

double terulet(int r)
{
    return r*r*3.14;
}

int main()
{
    int r;
    printf("Add meg a kor sugarat [egesz]: ");
    scanf("%d", &r);
    
    printf("Kerulet: %lf\n", kerulet(r));
    printf("Terulet: %lf\n", terulet(r));
}