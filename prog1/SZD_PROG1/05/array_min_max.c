#include <stdio.h>

// Tömb legkisebb eleme
int find_min(int n, int t[])
{
    int min=t[0];
    for (int i = 1; i < n; i++)
    {
        if (t[i] < min)
            min = t[i];
    }
    return min;
}

// Tömb legnagyobb eleme
int find_max(int n, int t[])
{
    int max=t[0];
    for (int i = 1; i < n; i++)
    {
        if (t[i] > max)
            max = t[i];
    }
    return max;
}

// Tömb kiíratása
void tomb_kiir(int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
}


int main ()
{
    int szamok[] = {5,21,53,3,12};
    int meret = 5;

    tomb_kiir(meret, szamok);
    printf("\nTomb legkisebb eleme: %d", find_min(meret, szamok));
    printf("\nTomb legnagyobb eleme: %d", find_max(meret, szamok));

    return 0;   
}