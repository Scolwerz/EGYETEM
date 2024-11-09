#include <stdio.h>
#include <stdlib.h>


#define LENGTH 26

void abece(char s[])
{
    for (int i=0; i<LENGTH; i++)
    {
        s[i]='a'+i;
    }
}
int main()
{
    char betuk[LENGTH+1];
    
    abece(betuk);
    betuk[LENGTH+1] = '\0';
    
    printf("%s", betuk);
    
    return 0;
}
