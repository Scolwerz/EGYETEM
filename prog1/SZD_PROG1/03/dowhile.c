#include <stdio.h>

int main()
{
    int szorzat= 1;
    int input = 1;

    do
    {
        szorzat *= input;
        printf("Adj meg egy számot: ");
        scanf("%d\n", &input);

    }
    while(input!=0);

    printf("Beírt számok szorzata: %d\n", szorzat);

    return 0;
}