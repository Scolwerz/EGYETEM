#include <stdio.h>
#include <stdlib.h>

int valid_triangle(int a, int b, int c)
{
    if ((a+b)>c && (a+c)>b && (b+c)>a)
	{
        return 1;
	}
    return 0;
}

int main()
{
    int a, b, c, result;

    printf("Add meg a haromszog oldalait [pozitiv egesz]: ");
    scanf("%d ", &a);
    scanf("%d ", &b);
    scanf("%d ", &c);

    result = valid_triangle(a,b,c);
    if (result == 1)
        printf("A haromszog megszerkesztheto.");
    else
        printf("A haromszog nem megszerkesztheto.");

    return 0;
}
