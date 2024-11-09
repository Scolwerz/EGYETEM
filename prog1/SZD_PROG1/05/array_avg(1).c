#include <stdio.h>

int array_sum(int n, int t[])
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += t[i];
    }
    return sum;
}

double array_avg(int n, int t[])
{
    return (double)array_sum(n,t) / (double)n;
}

int main ()
{
    int szamok[10]={21,52,3,4,9,6,7,2,1,10};
    int meret = 10;

    double atlag = array_avg(meret,szamok);
    printf("Atlag: %lf", atlag);

    return 0;   
}