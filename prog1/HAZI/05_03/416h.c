#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 1024

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void a_print(const int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
}

void sort(const int n, int t[])
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (t[j] > t[j+1])
            {
                swap(&t[j], &t[j+1]);
            }
        }
    }
}

int main(int argc, char* argv[])
{
    if (argc == 1)
    {
        fprintf(stderr, "Hiba! Adja meg egy szoveges allomany nevet!\n");
        exit(1);
    }
    
    char* fajlnev = argv[1];
    FILE *in = fopen(fajlnev, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Hiba! A(z) %s nevu file-t nem sikerult megnyitni!\n", argv[1]);
        exit(2);
    }

    char sor[BUFFER];
    int szamok[1000];
    int n = 0;
    while (fgets(sor, BUFFER, in) != NULL)
    {
        sor[strlen(sor)-1] = '\0';
        szamok[n] = atoi(sor);
        n++;
    }
    fclose(in);

    sort(n, szamok);
    a_print(n, szamok);
    
    return 0;
}