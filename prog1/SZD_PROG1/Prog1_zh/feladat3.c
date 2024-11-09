#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MERET 300

typedef struct
{
    int alatt, felett;
} Pair;


int get_random_number()
{
    int intmin = 25;
    int intmax = 875;   //Hiba: Jobbról nyílt --> intmax = 874
    int szam = rand();
    szam = szam % (intmax - intmin + 1) + intmin;

    return szam;
}

void feltolt(const int n, int tomb[])
{
    for (int i = 0; i < n; i++)
    {
        tomb[i] = get_random_number();
    }
}

int array_avg(const int n, const int tomb[])   //Hiba: double a visszatérés
{
    int array_avg = 0;   //Hiba: double
    for (int i = 0; i < n; i++)
    {
        array_avg += tomb[i];
    }
    array_avg /= n;   //Hiba: n castolás double-re

    return array_avg;
}

Pair alatt_felett(const int n, const int tomb[])
{
    Pair count = {0,0};
    int avg = array_avg(n, tomb);
    for (int i = 0; i < n; i++)
    {
        if (tomb[i] < avg)
        {
            count.alatt++;
        }
        else
        {
            count.felett++;
        }
    }

    return count;
}

int main()
{
    srand(1983);

    int szamok[MERET];
    feltolt(MERET, szamok);

    Pair result = alatt_felett(MERET, szamok);
    printf("Atlag alatti elemek szama: %d\nAtlag feletti elemek szama: %d\n", result.alatt, result.felett);

    return 0;
}