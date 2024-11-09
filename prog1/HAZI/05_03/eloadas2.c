#include <stdio.h>
#include <stdlib.h>

#define INITIAL_CAPACITY 2
#define MULTIPLIER 2

typedef struct {
    int *elems;
    int length;
    int capacity;
} DynArray;

void mem_error()
{
    fprintf(stderr, "Error: cannot allocate memory");
    exit(1);
}

DynArray * da_create()
{
    DynArray *result = malloc(sizeof(DynArray));
    if (result == NULL)
    {
        mem_error();
    }

    result->elems = malloc(INITIAL_CAPACITY * sizeof(int));
    if (result->elems == NULL)
    {
        mem_error();
    }
    result->length = 0;
    result->capacity = INITIAL_CAPACITY;
    
    return result;
}

void da_append(DynArray *self, int data)
{
    if (self->length == self->capacity)
    {
        int new_capacity = (int)(MULTIPLIER * self->capacity);
        self->elems = realloc(self->elems, new_capacity * sizeof(int));
        if (self->elems == NULL)
        {
            mem_error();
        }
        self->capacity = new_capacity;
    }
    self->elems[self->length] = data;
    self->length += 1;
}

void * da_destroy(DynArray *self)
{
    free(self->elems);
    free(self);
    return NULL;
}

double da_average(const DynArray *self)
{
    return da_sum(self) / self->length;
}

int da_sum(const DynArray *self)
{
    int sum = 0;
    for (int i = 0; i < self->length; i++)
    {
        sum += self->elems[i];
    }
    return sum;
}

int main()
{
    DynArray *szamok = da_create();
    int szam;
    
    
    FILE *in = fopen("numbers.txt", "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open \"numbers.txt\"");
        exit(1);
    }
    while (fscanf(in,"%d", &szam) == 1)
    {
        da_append(szamok, szam);
    }
    fclose(in);

    printf("%lf\n", da_average(szamok));

    szamok = da_destroy(szamok);

    return 0;
}