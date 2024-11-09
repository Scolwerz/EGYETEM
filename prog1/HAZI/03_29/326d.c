#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "prog1.h"

int get_int(string s)
{
    int x;
    printf("%s", s);
    scanf("%d", &x);
    return x;
}

int main()
{
    srand(time(NULL));
    
    int n = get_int("Hány darab számot kérsz: ");
    int min = get_int("Alsó határ: ");
    int max = get_int("Felső határ (zárt intervallum): ");
    printf("\nA generalt szamok: ");

    for (int i=0; i<n; i++)
    {
        int szam = rand();
        szam = (szam % (max-min+1)) + min;
        printf("%d ", szam);
    }

    return 0;
}