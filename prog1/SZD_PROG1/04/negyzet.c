#include <stdio.h>

int kerulet(int a)
{
    return 4*a;
}

int terulet(int a)
{
    return a*a;
}

int main()
{
    int a;
    printf("Add meg a negyzet oldalat: ");
    scanf("%d", &a);

    printf("Kerulet: %d\n", kerulet(a));
    printf("Terulet: %d\n", terulet(a));
}