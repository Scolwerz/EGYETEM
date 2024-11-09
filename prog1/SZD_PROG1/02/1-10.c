#include <stdio.h>

int main ()
{
    for (int i=1; i<=10; i++)
    {
        printf("%d\n", i);
    }

    printf("---------------\n");

    for (int i=10; i>0; i--)
    {
        printf("%d\n", i);
    }

    printf("---------------\n");

    for (int i=10; i>0; i--)
    {
        if (i%2 == 0)
        {
            printf("%d\n", i);
        }
    }
    
return 0;
}