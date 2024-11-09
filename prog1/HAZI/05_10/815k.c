#include <stdio.h>
#include <stdlib.h>

#define MAX 600

void kiir(const int n, int t[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (t[i] == 1)
        {
            printf("%d ", i + 1);
        }
    }
    puts("");
}

int main()
{
    int doors[MAX] = {0};
    
    for (int i = 1; i <= MAX; i++)
    {
        for (int j = i; j <= MAX; j += i)
        {
            doors[j - 1] = !doors[j - 1];
        }
    }

    kiir(MAX, doors);

    return 0;
}