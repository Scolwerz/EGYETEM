#include <stdio.h>

typedef struct
{
    int x, y;
} Pont;

void kiir(Pont p, const char* nev)
{
    printf("%s(%d, %d)\n", nev, p.x, p.y);
}

Pont origo()
{
    Pont origo = {0,0};
    return origo;
}

int main()
{
    // Pont a;
    // a.x=1;
    // a.y=2;
    Pont a = {1,2};
    Pont b = a;
    Pont c = origo();

    kiir(a, "A");
    kiir(b, "B");
    kiir(c, "C");

    return 0;
}