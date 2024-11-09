#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10

void kiir(int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]);
}

void arraystats(int n, int t[], int *min, int *max, double *atlag)
{
    *min = *max = t[0];
    *atlag = 0;

    for (int i = 0; i < n; i++)
    {
        *min = t[i] < *min ? t[i] : *min;
        *max = t[i] > *max ? t[i] : *max;
        *atlag += t[i];
    }
    *atlag /= n;
}


int main()
{
    srand(time(NULL));
    int intmin=10, intmax=99, szam;
    int szamok[MAX];
    int min, max;
    double atlag;
    
    for (int i=0; i<MAX; i++)
    {
        szam = rand();
        szamok[i] = (szam % (intmax-intmin+1)) + intmin;
    }
    
    printf("A tömb elemei: ");
    kiir(MAX, szamok);
    
    arraystats(MAX, szamok, &min, &max, &atlag);
    
    printf("Legkisebb elem: %d\n", min);
    printf("Legnagyobb elem: %d\n", max);
    printf("Az elemek átlaga: %.2f\n", atlag);


    return 0;
}