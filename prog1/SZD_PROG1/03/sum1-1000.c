#include <stdio.h>

int main()
{
    int a,b;

    printf("Add meg az intervallum első elemét: ");
    scanf("%d\n", &a);
    printf("Add meg az intervallum második elemét:");
    scanf("%d\n", &b);

    int osszeg = 0;

    for(int i = a; i<=b; ++i)
    {
        osszeg += i;
    }

    printf("Számok összege: %d\n", osszeg);

    return 0;
}