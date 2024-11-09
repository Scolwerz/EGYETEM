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

int palindrom(int n, int t[])
{
    for (int i = 0; i < n/2; i++)
    {
        if (t[i] != t[n-1-i])
            return 0;
    }
    return 1;
}


int main ()
{
    int szamok[] = {1,2,3,1};
    int meret = 4;

    int result = palindrom(meret, szamok);
    tomb_kiir(meret, szamok);
    puts("");
    array_reverse(meret, szamok);
    tomb_kiir(meret, szamok);
    puts("");
    if (result == 1) printf("Palindrom.");
    else printf("Nem palindrom.");

    return 0;   
}