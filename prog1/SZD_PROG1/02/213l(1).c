#include <stdio.h>

int main ()
{
    int x, p=0, n=0;

    do
    {
        printf("Egesz szam (vege: 0): ");
        scanf("%d", &x);
        if (x>0)
            p++;
        else if (x != 0)
            n++;
    }
    while (x!=0);

    printf("\nPozitiv elemek szama: %d\n", p);
    printf("\nNegativ elemek szama: %d\n", n);

    return 0;
}