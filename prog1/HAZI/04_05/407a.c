#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10

typedef struct
{
    int max, min;
    double avg;
} Stats;

void kiir(int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]);
}

Stats arraystats(int n, int t[])
{
    Stats x;
    x.min = x.max = t[0];
    for (int i=0; i<n; i++)
    {
        x.min = t[i] < x.min ? t[i] : x.min;
        x.max = t[i] > x.max ? t[i] : x.max;
        x.avg += t[i];
    }
    x.avg /= MAX;
    return x;
}

int main()
{
    srand(time(NULL));
    Stats result;
    int intmin=10, intmax=99;
    int szamok[MAX];
    for (int i=0; i<MAX; i++)
    {
        int szam = rand();
        szamok[i] = (szam % (intmax-intmin+1)) + intmin;
    }
    kiir(MAX, szamok);
    result = arraystats(MAX, szamok);
    printf("Legkisebb elem: %d\nLegnagyobb elem: %d\nAz elemek atlaga: %lf", result.min, result.max, result.avg);

    return 0;
}