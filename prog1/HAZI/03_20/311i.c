#include <stdio.h>
#include <stdlib.h>

int main()
{
    for (int i=1; i<=100; i++)
    {
        if (i%15 == 0)  // i%3 == 0 && i%5 == 0
        {
            printf("fizzbuzz\n");
        }
        else if (i%3 == 0)
        {
            printf("fizz\n");
        }
        else if (i%5 == 0)
        {
            printf("buzz\n");
        }
        else
        {
            printf("%d\n", i);
        }
    }

    /*
    for (int i=1; i<=100; i++)
    {
        if (i%15 == 0)  // i%3 == 0 && i%5 == 0
        {
            if (i%3 == 0)
            {
                printf("fizz");
            }
            if (i%5 == 0)
            {
                printf("buzz");
            }
            printf("  ");
            continue;
        }
        printf("%d  ", i);
    }
    
    printf("\n\n\n")
    
    for(int i=1 ;i<=100; i++)
    {
        printf(i%3 ? i%5 ? "%d  " : "buzz  " : (i%5 ? "fizz  " : "fizzbuzz  "), i);
    }
    */
    
    return 0;
}
