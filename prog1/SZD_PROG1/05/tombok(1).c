#include <stdio.h>

void tomb_kiir(int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
}

int array_sum(int n, int t[])
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += t[i];
    }
    return sum;
}

int main ()
{
    int szamok[10]={1,2,3,4,5,6,7,8,9,10};
    int meret = 10;

    // tomb_kiir(meret, szamok);

    int osszeg = array_sum(meret,szamok);
    printf("Osszeg: %d", osszeg);

    return 0;   
}