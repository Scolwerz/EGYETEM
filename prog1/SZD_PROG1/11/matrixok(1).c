#include <stdio.h>
#include <stdlib.h>

void print_matrix(const int n, const int m, int t[n][m])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", t[i][j]);
        }
        puts("");
        
    }
}

int matrix_sum(const int n, const int m, int t[n][m])
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            sum += t[i][j];
        }    
    }

    return sum;
}

int main()
{
    // int szamok[] = {23,1,53,523,13,2};
    // int n = sizeof(szamok) / sizeof(szamok[0]);

    int matrix[/*4*/][6] = {
        {1,2,5,3,2,4},
        {0,2,3,5,0,2},
        {2,5,0,7,0,1},
        {2,5,6,1,3,7}
    };
    int sorok = 4, oszlopok = 6;

    print_matrix(sorok, oszlopok, matrix);
    puts("");
    printf("Matrix osszege: %d\n", matrix_sum(sorok, oszlopok, matrix));

    return 0;
}