#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int n, min, max;

    srand(time(NULL));

    printf("Hany darab szamot kersz: ");
    scanf("%d", &n);
    printf("Also hatar: ");
    scanf("%d", &min);
    printf("Felso hatar (zart intervallum): ");
    scanf("%d", &max);
    printf("\nA generalt szamok: ");

    for (int i=0; i<n; i++)
    {
        int szam = rand();
        szam = (szam % (max-min+1)) + min;
        printf("%d ", szam);
    }

    return 0;
}