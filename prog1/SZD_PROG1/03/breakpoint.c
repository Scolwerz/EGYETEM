#include <stdio.h>

int main()
{
    for(int i=1; i<=1000; ++i)
    {
        if(i % 7 == 0 && i % 3 == 0)
        {
            printf(" %d \n", i);
            break;
        }
    }

    return 0;
}