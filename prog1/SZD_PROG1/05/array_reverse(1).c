#include <stdio.h>

void array_reverse(int n, int t[])
{
    int temp;
    for (int i = 0; i < n/2; i++)
    {
        temp = t[i];
        t[i]=t[n-1-i];
        t[n-1-i]=temp;
    }
}

void tomb_kiir(int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
}

int main ()
{
    int szamok[] = {8,7,34,62,41};
    int meret = 5;

    tomb_kiir(meret, szamok);
    printf("\n");
    array_reverse(meret, szamok);
    tomb_kiir(meret, szamok);
    return 0;   
}