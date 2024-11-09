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

int get_random(int intmin, int intmax)
{
    int szam = rand();
    szam = szam % (intmax-intmin+1) + intmin;
    return szam;
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
    int szamok[MAX];
    
    for (int i=0; i<MAX; i++)
    {
        szamok[i] = get_random(10,99);
    }
    
    printf("A tomb elemei: ");
    kiir(MAX, szamok);
    
    result = arraystats(MAX, szamok);
    printf("Legkisebb elem: %d\nLegnagyobb elem: %d\nAz elemek atlaga: %.2lf", result.min, result.max, result.avg);

    return 0;
}