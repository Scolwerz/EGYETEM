#include <stdio.h>
#include <stdlib.h>

void elemek(int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]);
}

int main()
{
    int t[] = {5,11,7,9,43,3,82};
    int n = 7;
    
    elemek(n,t);
    
    return 0;
}