#include <stdio.h>
#include <stdlib.h>


#define LENGTH 26   //abc betuinek szama

void abece(int n, char s[])
{
    for (int i=0; i<n; i++)
    {
        s[i]='a'+i;
    }
    s[n] = '\0';
}

int main()
{
    char betuk[LENGTH+1];
    
    abece(LENGTH,betuk);
    
    printf("%s", betuk);
    
    return 0;
}
