#include<stdio.h>

void print_tomb(int meret, int tomb[])
{
    for(int i=0; i<meret; ++i)
    {
        printf("%d\n", tomb[i]);
    }
}

int main()
{
    int szamok [5]={99,1,2,3,4};
    print_tomb(5,szamok);
    return 0;
}
