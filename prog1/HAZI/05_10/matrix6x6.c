/* Hozzon létre a main() fv.-ben egy 6 x 6 méretű mátrixot.
Egy eljárássegítségével írassa ki a mellékátló elemeit. */
#include <stdio.h>
#include <stdlib.h>

void mellekatlo(int n, int matrix[n][n])
{
    for (int i = n-1; i >= 0; i--)
    {
        printf("%d\t", matrix[n-1 - i][i]);
    }
}
int main()
{
    int n = 6;
    int matrix[6][6] = {
    {2,5,1,5,2,0},
    {5,11,6,1,7,1},
    {4,7,1,7,3,9},
    {1,8,4,7,23,0},
    {7,9,22,1,0,6},
    {10,6,3,1,9,4}
    };

    mellekatlo(n, matrix);
    
    return 0;
}