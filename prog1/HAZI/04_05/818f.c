#include <stdio.h>
#include <stdlib.h>

#define SZAMOK 100

int negyzetosszeg()
{
    int sum=0;
    for (int i=1; i<=SZAMOK; i++)
    {
        sum += (i*i);
    }
    return sum;
}
int osszegnegyzete()
{
    int sum=0;
    for (int i=1; i<=SZAMOK; i++)
    {
        sum += i;
    }
    return sum*sum;
}

int main()
{
    printf("Elso 100 szam osszegenek negyzete es negyzetosszegenek kulonbsege: %d\n", osszegnegyzete()-negyzetosszeg());

    return 0;
}