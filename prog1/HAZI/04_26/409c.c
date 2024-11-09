#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1000

int main(int argc, char* argv[])
{
    if (argc == 1)
    {
        fprintf(stderr, "Hiba! Adja meg egy szoveges allomany nevet!\n");
        exit(1);
    }
    
    char* fajlnev = argv[1];
    FILE *fp = fopen(fajlnev, "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Hiba! A %s nevu file-t nem sikerult megnyitni!\n", argv[1]);
        exit(2);
    }

    char sor[MAX];
    int db = 0;

    printf("#### Fajl Tartalma: ####\n");
    while (fgets(sor, MAX, fp) != NULL)
    {
        sor[strlen(sor)-1] = '\0';
        printf("%s\n", sor);
        db++;
    }
    printf("########################\n\n");

    fclose(fp);

    printf("Sorok szama: %d\n", db);
    
    return 0;
}