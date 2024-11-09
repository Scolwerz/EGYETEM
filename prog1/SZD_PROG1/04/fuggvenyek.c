#include <stdio.h>
#include <stdlib.h>

int sum(int n1, int n2)
{
    return n1 + n2;
}

int dupla(int n)
{
    return 2*n;
}

int myabs(int n)
{
    return (n<0) ? -1*n : n;
}

void print_nev(int n)
{
    for(int i=0; i<n; ++i)
    {
        puts("Mark");
    }
}

int main()
{
    print_nev(2);
    return 0;
}