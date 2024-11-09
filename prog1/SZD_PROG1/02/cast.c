#include <stdio.h>

int main ()
{
    int a=20, b=3;
    int result = a/b;

    printf("a / b = %d\n", result);
    printf("20 / 3 = %d\n", 20 / 3);
    printf("20.0 / 3 = %lf\n", 20.0 / 3);
    printf("a / b = %lf\n", (double)a / (double)b);
    
    return 0;
}