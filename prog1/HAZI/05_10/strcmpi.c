/* Implementálja az int strcmpi(const char* s1, const char* s2);
szignatúrával rendelkező függvényt. A fv. hasonlóan működjön az strcmp()
fv.-hez, de a kis- és nagybetűket NE különböztesse meg. Vagyis pl. az "ez"
és az "EZ" szavakat tekintse egyformáknak. */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int strcmpi(const char* s1, const char* s2)
{
    int length = strlen(s1);
    for (int i = 0; i < length; i++)
    {
        if (toupper(s1[i]) != toupper(s2[i]))
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    char* s1 = "asdfgh";
    char* s2 = "asdfgh";
    char* s3 = "aSDfgH";
    char* s4 = "asdgh";
    
    printf("s1, s2: %d\n", strcmpi(s1, s2));
    printf("s1, s3: %d\n", strcmpi(s1, s3));
    printf("s1, s4: %d\n", strcmpi(s1, s4));
    
    return 0;
}