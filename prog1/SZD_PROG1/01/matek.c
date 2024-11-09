#include <stdio.h>

int main()
{
    int a=7,b=3;
    printf("Osszeg: %d\n", a+b);
    printf("Kulonbseg: %d\n", a-b);
    printf("Szorzat: %d\n", a*b);
    printf("Hanyados: %d\n", a/b);
    printf("7.0/3.0 = %lf\n", 7.0/3.0);
    printf("%d %% %d = %d\n", a, b, a%b);
    
    int x;
    printf("Adj meg egy szamot: ");
    scanf("%d", &x);
    if (x%2 == 0)
        printf("A szam paros");
    else
        printf("A szam paratlan");
    
    
    
    
    
    
    return 0;
}
