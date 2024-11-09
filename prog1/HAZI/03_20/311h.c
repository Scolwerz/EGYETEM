#include <stdio.h>
#include "prog1.h"

void line(char c, int length)
{
    for (int i=0; i<length; i++)
    {
        printf("%c", c);
    }
    puts("");
}

int main()
{
    printf("Hello\n");
    line('-', 20);
    printf("World\n");
    
    return 0;
}
