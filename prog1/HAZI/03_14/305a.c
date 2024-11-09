#include <stdio.h>
#include <stdlib.h>

int rendezett(int n, int t[])
{
    for (int i=1; i<n; i++)
    {
        if (t[i-1]>t[i])
            return 0;
    }
    return 1;
}


int main()
{
    int t[] = {3,5,11,7,9,43,76,82};
    int n = 8;

    if (rendezett(n,t) == 1)
        printf("A tomb rendezett");
    else
        printf("A tomb nem rendezett");


    return 0;
}