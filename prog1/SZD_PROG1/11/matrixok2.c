#include <stdio.h>
#include <stdlib.h>

void print_matrix(const int n, int t[n][n])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d  ", t[i][j]);
        }
        puts("");
    }
}

int matrix_sum(const int n, int t[n][n])
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            sum += t[i][j];
        }    
    }

    return sum;
}

void print_foatlo(const int n, int t[n][n])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", t[i][i]);
    }
}

int main()
{
    // int szamok[] = {23,1,53,523,13,2};
    // int n = sizeof(szamok) / sizeof(szamok[0]);

    int matrix[/*4*/][4] = {
        {1,2,2,4},
        {0,2,0,2},
        {2,5,0,1},
        {2,1,3,7}
    };
    int n = 4;

    print_matrix(n, matrix);
    printf("Matrix osszege: %d\n", matrix_sum(n, matrix));
    printf("\nFoatlo:\n");
    print_foatlo(n, matrix);

    return 0;
}