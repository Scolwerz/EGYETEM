#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 1024

int  get_num_lines(char* filename)
{
    int n_lines = 0;

    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFSIZE];
    while (fgets(line, BUFSIZE, in) != NULL)
    {
        line[strlen(line)-1] = '\0';
        n_lines++;
    }
    fclose(in);

    return n_lines;
}

int * file_read_to_array(const int n, const char* filename)
{
    int *t = malloc(n * sizeof(int));
    if (t == NULL)
    {
        fprintf(stderr, "Error: cannot allocate memory %s\n", filename);
        exit(1);
    }

    int i = 0;
    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFSIZE];
    while (fgets(line, BUFSIZE, in) != NULL)
    {
        int num = atoi(line);
        t[i] = num;
        i++;
    }
    fclose(in);

    return t;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void quicksort(int t[], const int bal, const int jobb)
{
    int i = bal, j = jobb;
    int x = t[(bal+jobb) / 2];
    while (i <= j)
    {
        while (t[i] < x) ++i;
        while (t[j] > x) --j;
        if (i <= j)
        {
            swap(&t[i], &t[j]);
            ++i;
            --j;
        }
    }
    if (bal < j)  quicksort(t, bal, j);
    if (i < jobb) quicksort(t, i, jobb);
}

void print_array(const int n, int t[])
{
    for (int i=0; i<n; i++)
    {
        printf("%d ", t[i]);
    }
    puts("");
}

int main()
{
    char* filename = "millions.txt";

    int sorok_szama = get_num_lines(filename);

    int *tomb = file_read_to_array(sorok_szama, filename);

    quicksort(tomb, 0, sorok_szama-1);

    print_array(sorok_szama, tomb);

    free(tomb);

    return 0;
}
