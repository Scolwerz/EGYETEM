#include <stdio.h>
#include <stdlib.h>

void kiir(int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]);
    
}

int main()
{
    int n;

    printf("Hany db szamot szeretnel bevinni: ");
    scanf("%d", &n);

    int szamok[n];
    int absszamok[n];

    for (int i=0; i<n; i++)
    {
        printf("\n%d. szam: ", i+1);
        scanf("%d", &szamok[i]);
        absszamok[i] = abs(szamok[i]);
    }
    puts("");

    printf("A bevitt szamok abszolutertekei: ");
    kiir(n, absszamok);
    printf("A megadott szamok: ");
    kiir(n, szamok);

    return 0;
}