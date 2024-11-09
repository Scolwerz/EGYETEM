#include <stdio.h>

int main()
{
    for (int i=1; i<=10; i++)
    {
        printf("%d\n", i);
        if (i == 5)
            break;
        printf("#iteracio vege\n");
    }
    printf("END");

    return 0;
}