#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int get_int(char* s)
{
    int x;
    printf("%s", s);
    scanf("%d", &x);
    return x;
}

int get_random(int intmin, int intmax)
{
    int szam = rand();
    szam = szam % (intmax-intmin+1) + intmin;
    return szam;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(const int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        for (int j=0; j<n-i-1; j++)
        {
            if (t[j] > t[j+1])
            {
                swap(&t[j], &t[j+1]);
            }
        }
    }
}

void kiir(const int n, int t[])
{
    for (int i=0; i<n; i++)
    {
        printf(" %d", t[i]);
    }
}

int main()
{
    srand(time(NULL));
    const int n = get_int("Hany darab szamot kersz: ");
    int intmin = get_int("Also hatar: ");
    int intmax = get_int("Felso hatar (zart intervallum): ");
    int szamok[n], szam;
    int j=0, uj, db=n;

    szamok[0] = get_random(intmin,intmax);
    j++;
    db--;
    while (db != 0)
    {
        uj = 1;
        szam = get_random(intmin,intmax);
        for (int i=0; i<j; i++)
        {
            if (szam == szamok[i])
            {
                uj=0;
            }
        }
        if (uj == 1)
        {
            szamok[j]=szam;
            j++;
            db--;
        }
    }
    
    kiir(n, szamok);
    
    sort(n, szamok);

    printf("\nA generalt szamok:");
    kiir(n, szamok);

    return 0;
}