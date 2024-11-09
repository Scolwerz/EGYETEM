#include <stdio.h>
#include <stdlib.h>
#include "prog1.h"

void kiir(string s, int n, int t[])
{
    printf("%s", s);
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]); 
}

int get_int(string s)
{
    printf("%s", s);
    int x;
    scanf("%d", &x);
    return x;
}

int main()
{
    int n = get_int("Hany db számot szeretnél bevinni: ");
    int szamok[n];
    int abs_szamok[n];

    for (int i=0; i<n; i++)
    {
        szamok[i] = get_int("Szám: ");
        abs_szamok[i] = abs(szamok[i]);
    }
    puts("");

    kiir("A bevitt számok abszolútértékei: ", n, abs_szamok);
    kiir("A megadott számok: ", n, szamok);

    return 0;
}