#include <stdio.h>

int array_prod(int n, int t[])
{
    int prod = 1;
    for (int i = 0; i < n; i++)
    {
            prod *= t[i];
    }
    return prod;
}

int main ()
{
    int t[3]={3,4,5};
    int meret = 3;

    int prod = array_prod(meret,t);
    printf("Szorzat: %d", prod);

    return 0;   
}