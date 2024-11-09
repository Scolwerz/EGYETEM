#include <stdio.h>

int kerulet(int a, int b)
{
    return 2*(a+b);
}

int terulet(int a, int b)
{
    return a*b;
}

int main()
{
    int a,b;
    printf("Add meg a teglalap oldalait: ");
    scanf("%d\n", &a);
    scanf("%d", &b);
    printf("Kerulet: %d\n", kerulet(a,b));
    printf("Terulet: %d\n", terulet(a,b));
}