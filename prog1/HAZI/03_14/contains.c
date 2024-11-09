#include <stdio.h>
#include <stdlib.h>

int contains(int n, int t[], int x)
{
    for (int i=0; i<n; i++)
    {
        if (t[i] == x)
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    int t[] = {5,11,7,9,43,3,82};
    int n = 7;
    int x;
    
    printf("Adj meg egy szamot [egesz]: ");
    scanf("%d", &x);
    if (contains(n,t,x) == 1)
        printf("Tartalmazza");
    else
        printf("Nem tartalmazza");

    return 0;
}