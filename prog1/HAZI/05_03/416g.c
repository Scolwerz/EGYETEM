#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int get_random(int intmin, int intmax)
{
    return rand() % (intmax-intmin+1) + intmin;
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void shuffle(int n, int tomb[])
{
    for (int i = n-1; i > 0; i--)
    {
        int j = get_random(0,i);
        swap(&tomb[i], &tomb[j]);
    }
}

void a_print(const int n, int t[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", t[i]);
    }
}

int main()
{
    srand(time(NULL));

    int szamok[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    int meret = sizeof(szamok) / sizeof(szamok[0]);
    printf("Tomb elemei: ");
    a_print(meret, szamok);

    puts("");

    shuffle(meret, szamok);
    printf("Utana: ");
    a_print(meret, szamok);

    return 0;
}