#include <stdio.h>
#include <stdlib.h>

int main()
{
    int tomb[10] = {1,2,3};

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", tomb[i]);
    }
    
    int meret = 10;
    int tomb2[meret] = {1,2,3};
    for (int i = 0; i < meret; i++)
    {
        printf("%d ", tomb2[i]);
    }

    return 0;
}