#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n = 309;
    char szamjegyek[n+1];
    for (int i=0; i<n; i++)
    {
        szamjegyek[i]='0';
    }
    szamjegyek[n] = '0'+1;
    szamjegyek[n-1] = '1';
    
    int maradek = 0;
    int szam;
    for (int i=0; i<1024; i++)
    {
        for (int j=n-1; j>=0; j--)
        {
            szam = (szamjegyek[j]-'0')*2+maradek;
            if (szam > 9)
            {
                maradek = 1;
                szam -= 10;
            }
            else
            {
                maradek = 0;
            }
            szamjegyek[j] = szam+'0';
        }
    }
    
    printf("2^1024 = %s", szamjegyek);
    
    int sum = 0;
    for (int i=1; i<n; i++)
    {
        sum += abs(szamjegyek[i] - szamjegyek[i-1]);
    }
    printf("\n\nMegoldas: %d", sum);

    return 0;
}
