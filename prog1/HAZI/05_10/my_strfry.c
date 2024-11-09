/* Írja meg a my_strfry() eljárást. Ez kap egy sztringet, amiben a karaktereket
összekeveri. Ez az eljárás helyben módosítsa a sztringet! A programot lehessen
Windows alatt is futtatni. Korábban már volt egy házi feladat, amiben egy
tömb elemeit kellett összekeverni; annak a kódját újra lehethasznosítani. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void swap(char *a, char *b)
{
    char temp = *a;
    *a = *b;
    *b = temp;
}

void my_strfry(char *s)
{
    int length = strlen(s);
    for (int i = 0; i < length - 1; i++)
    {
        int range = length -i;
        int j = i + rand() % range;
        swap(&s[i], &s[j]);
    }
}

int main()
{
    srand(time(NULL));
    
    char text[] = "asdfghjkl";

    my_strfry(text);
    printf("%s\n", text);

    return 0;
}