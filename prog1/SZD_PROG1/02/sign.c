#include <stdio.h>

int main()
{
    int x;
    
    printf("Adj meg aegy szamot: ");
    scanf("%d", &x);
    if (x==0) {
        printf("0");
    }
    else if (x<0) {
        printf("negativ");
    }      
    else {
        printf("pozitiv");
    }

    return 0;
    
}