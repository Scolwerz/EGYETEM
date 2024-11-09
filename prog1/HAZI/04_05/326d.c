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
    int intmin = get_int("Alsó határ: ");
    int intmax = get_int("Felső határ (zárt intervallum): ");
    int szamok[n];
    int j=1;
    int kov;
    int db=n;
    
    int szam = rand();
    szamok[0] = (szam % (intmax-intmin+1)) + intmin;
    db--;
    while (db != 0)
    {
        kov = 0;
        szam = rand();
        szam = (szam % (intmax-intmin+1)) + intmin;
        for (int i=0; i<j; i++)
        {
            if (szam == szamok[i])
            {
                kov=1;
            }
        }
        if (kov == 0)
        {
            szamok[j]=szam;
            j++;
            db--;
        }
    }
    
    
    printf("\nA generált számok: ");
    for (int i=0; i<n; i++)
    {
        printf("%d ", szamok[i]);
    }
    
    
    return 0;
}