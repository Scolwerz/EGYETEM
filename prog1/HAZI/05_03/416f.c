#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int get_random(int intmin, int intmax)
{
    int szam = rand();
    szam = szam % (intmax-intmin+1) + intmin;
    return szam;
}

int choice(const int n, const int tomb[])
{
    return tomb[get_random(0, n-1)];
}

void a_print(const int n, int t[])
{
    for (int i = 0; i < n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]);
}

int main()
{
    srand(time(NULL));
    
    int szamok[] = {4,21,53,26,123,11,4,21,2,0,56,643,32,34,1,24};
    int meret = sizeof(szamok) / sizeof(szamok[0]);
    
    printf("Tome elemei: ");
    a_print(meret, szamok);
    
    int result = choice(meret, szamok);
    printf("A tomb egy veletlenszeru eleme: %d", result);
    
    return 0;
}