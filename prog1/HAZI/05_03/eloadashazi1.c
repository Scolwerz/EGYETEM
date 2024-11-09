#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int get_random(int intmin, int intmax)
{
    return rand() % (intmax - intmin + 1) + intmin;
}

int main()
{
    srand(time(NULL));

    FILE *out = fopen("numbers.txt","w");
    if (out == NULL)
    {
        fprintf(stderr, "\"A numbers.txt\" fajlt nem sikerult megnyitni!");
        exit(1);
    }
    for (int i = 0; i < 100; i++)
    {
        fprintf(out, "%d\n", get_random(10,99));
    }
    printf("# Fajl letrehozva");
    fclose(out);
    
    return 0;
}