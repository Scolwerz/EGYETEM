#include <stdio.h>
#include <stdlib.h>
#include "prog1.h"

#define SIZE 200

int get_int(string s)
{
    printf("%s", s);
    int x;
    scanf("%d", &x);
    return x;
}

void kiir(int n, int t[])
{
    for (int i=0; i<n-1; i++)
    {
        printf("%d, ", t[i]);
    }
    printf("%d\n", t[n-1]); 
}

int main()
{
    int x, tmp, n1=0, n2=0, c=0;
    int szamok[SIZE], different[SIZE];
    printf("Adj meg 0 vegjelig egesz szamokat az [1, 99] intervallumbol!\n");
    
    while (x != 0)
    {
        x = get_int("Szam: ");
        
        if (x == 0) break;
        else if (x < 0 || x > 99)
        {
            printf("Ez a szam kivul esik az elfogadhato intervallumon!\n");
        }
        else
        {
            szamok[n1] = x;
            c=0;
            for (int i=0; i<n1; i++)
            {
                if (szamok[n1] == szamok[i])
                {
                    c++;
                }
            }
            if (c == 0)
            {
                different[n2] = szamok[n1];
                n2++;
            }
            n1++;
        }
    }
    puts("");
    for (int i=0; i<n2-1; i++)
    {
        for (int j=n2-1; j>i; j--)
        {
            if (different[j] < different[i])
            {
                tmp = different[i];
                different[i] = different[j];
                different[j] = tmp;
            }
        }
    }

    
    printf("%d db kulonbozo szam lett megadva.\nEzek (novekvo sorrendben): ", n2);
    kiir(n2, different);
    
    return 0;
}