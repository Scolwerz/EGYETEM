#include <stdio.h>
#include <stdlib.h>

void rendez(const int meret, int tomb[])
{
    int i, j, temp;
    for (i = 0; i < meret - 1; ++i)
    {
        for (j = i + 1; j < meret; ++j)
        {
            if (tomb[j] < tomb[i])
            {
                temp = tomb[i];
                tomb[i] = tomb[j];
                tomb[j] = temp;
            }
        }
    }
}

void a_print(const int n, int t[])
{
    for (int i=0; i<n; i++)
    {
        printf("%d ", t[i]);
    }
}

int * sorted(const int n, const int t[])
{
    int *copy = malloc(n*sizeof(int));
    for (int i = 0; i < n; i++)
    {
        copy[i] = t[i];
    }
    rendez(n, copy);

    return copy;
}


int main()
{
    int tomb[] = {12,4,35,6,43,120,42,53,1};
    int meret = sizeof(tomb) / sizeof(tomb[0]);
    a_print(meret, tomb);
    puts("");
    
    int *rendezett = sorted(meret, tomb);
    a_print(meret, tomb);
    puts("");
    a_print(meret, rendezett);

    return 0;
}