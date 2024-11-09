#include <stdio.h>

int main()
{
    int x,y,k,t;
    
    printf("Add meg a teglalap 2 szomszedos oldalat: ");
    scanf("%d", &x);
    scanf("%d", &y);
    k = 2*(x+y);
    t = x*y; 
    printf("A teglalap kerulete: %d\n", k);
    printf("A teglalap terulete: %d\n", t);
    
    return 0;
}
