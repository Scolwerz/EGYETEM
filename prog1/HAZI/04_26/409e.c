#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *in = fopen("in.txt", "r");
    FILE *out = fopen("out.txt", "w");
    if (in == NULL)
    {
        printf("Hiba: Nem sikerult megnyitni a fajlt!\n");
        exit(1);
    }
    printf("# in.txt sikeresen megnyitva\n");
    
    double szam;
    int counter = 0;
    
    printf("# 0,5-nel nagyobb szamok szurese...\n");
    while (fscanf(in, "%lf", &szam) == 1)
    {
        if (szam > 0.5)
        {
            fprintf(out, "%.15lf\n", szam);
            counter++;
        }
    }
    printf("# szures vege\n");
    
    fclose(in);
    fclose(out);
    printf("# out.txt bezarva\n");
    
    printf("# out.txt-be kiirt szamok mennyisege: %d db\n", counter);
    
    return 0;
}