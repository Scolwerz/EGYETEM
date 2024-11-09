#include <stdio.h>

int main()
{
    int n;
        printf("Adja meg a gyémánt magasságát [páratlan]: ");
        scanf("%d", &n);
    if (n%2 == 0)
    {
        printf("Hibas bemenet.");
    }
    else
    {
        for (int i = 0; i<n/2+1; ++i)
        {
            for(int j =0; j<n/2-i; ++j)
            {
            printf(" ");
            }

            for(int j =0; j<2*i+1; ++j)
            {
            printf("*");
            }
            puts("");
        }

        for( int i = n/2; i>0; --i)
        {
            for(int j =0; j<=n/2-i; ++j)
            {
            printf(" ");
            }

            for(int j =0; j<2*i-1; ++j)
            {
            printf("*");
            }
            puts("");
        }
    }
    return 0;
}