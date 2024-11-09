#include <stdio.h>

void rendez(const int meret, int tomb[])
{
    int i, j, temp;
    for (i = 0; i < meret - 1; ++i)
    {
        for (j = i + 1; j < meret; ++j)
        {
            if (tomb[j] < tomb[i])
            {
                temp = tomb[i];
                tomb[i] = tomb[j];
                tomb[j] = temp;
            }
        }
    }
}

void kiir(const int meret, int tomb[])
{
    for (int i = 0; i < meret; i++)
    {
        printf("%d ", tomb[i]);
    }
    puts("");
}

int main()
{
    int tomb[] = {12,52,53,31,10,3};
    int meret = sizeof(tomb) / sizeof(tomb[0]);

    kiir(meret, tomb);
    rendez(meret, tomb);
    kiir(meret, tomb);
}