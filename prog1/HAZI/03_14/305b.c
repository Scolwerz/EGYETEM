#include <stdio.h>
#include <stdlib.h>

int legkisebb(int n, int t[])
{
    int x=t[0];
    for (int i=1; i<n; i++)
    {
        if (t[i] < x)
        {
            x = t[i];
        }
    }
    return x;
}

int legnagyobb(int n, int t[])
{
    int x=t[0];
    for (int i=1; i<n; i++)
    {
        if (t[i] > x)
        {
            x = t[i];
        }
    }
    return x;
}

int main()
{
    int t[] = {5,11,7,9,43,3,82};
    int n = 7;

    printf("A tomb legkisebb eleme: %d\n", legkisebb(n,t));
    printf("A tomb legnagyobb eleme: %d\n", legnagyobb(n,t));

    return 0;
}