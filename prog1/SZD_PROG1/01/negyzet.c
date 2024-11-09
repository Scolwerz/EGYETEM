#include <stdio.h>

int main()
{
    int x,k,t;
    printf("Add meg a negyzet oldalat: ");
    scanf("%d", &x);
    k = 4*x;
    t = x*x; 
    printf("A negyzet kerulete: %d\n", k);
    printf("A negyzet terulete: %d\n", t);
    return 0;
}
