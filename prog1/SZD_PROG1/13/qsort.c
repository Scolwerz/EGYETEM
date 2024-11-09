#include <stdio.h>
#include <stdlib.h>

/*
- ha bal < jobb ---> negatív
- ha bal = jobb ---> 0
- ha bal > jobb ---> pozitív
*/
int cmp(const void *bal, const void *jobb)
{
    /*const int *a = bal;
    const int *b = jobb;
    return *a - *b;*/
    return *(const int*)bal - *(const int*)jobb;
}

void kiir(int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
    puts("");
}

int main()
{
    int szamok[] = {123,24,35,642,34,10,23,6};
    int meret = sizeof(szamok) / sizeof(szamok[0]);

    qsort(szamok, meret, sizeof(int), cmp);

    kiir(meret, szamok);

    return 0;
}