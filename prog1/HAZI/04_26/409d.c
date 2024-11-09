#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp = fopen("valos_szamok.txt", "r");
    if (fp == NULL)
    {
        printf("Hiba: Nem sikerult megnyitni a fajlt!\n");
        exit(1);
    }
    
    double szam;
    double sum = 0;

    while (fscanf(fp, "%lf", &szam) != 0)
    {
        sum += szam;
    }

    fclose(fp);

    printf("Szamok osszege: %.20lf\n", sum);
    
    return 0;
}