/*Rendezzük a millions.txt fájl (link) tartalmát az
előadáson vett dinamikus tömb adatszerkezet használatával. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 1024
#define INITIAL_CAPACITY 2
#define MULTIPLIER 1.5

typedef struct {
    int *elems;
    int length;
    int capacity;
} DynArray;

void mem_error() {
    fprintf(stderr, "Error: cannot allocate memory");
    exit(1);
}

DynArray * da_create() {
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

void da_append(DynArray *self, int data) {
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

void * da_destroy(DynArray *self) {
    free(self->elems);
    free(self);
    return NULL;
}

void da_print(DynArray *self) {
    for (int i = 0; i < self->length; i++)
    {
        printf("%d ", self->elems[i]);
    }
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void da_sort(DynArray *self, const int bal, const int jobb) {
    int i = bal, j = jobb;
    int x = self->elems[(bal+jobb) / 2];
    while (i <= j)
    {
        while (self->elems[i] < x) ++i;
        while (self->elems[j] > x) --j;
        if (i <= j)
        {
            swap(&self->elems[i], &self->elems[j]);
            ++i;
            --j;
        }
    }
    if (bal < j)  da_sort(self, bal, j);
    if (i < jobb) da_sort(self, i, jobb);
}

int main()
{
    DynArray *szamok = da_create();
    
    char* fajlnev = "millions.txt";
    FILE *in = fopen(fajlnev, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", fajlnev);
        exit(1);
    }

    char sor[BUFFER];
    while (fgets(sor, BUFFER, in) != NULL)
    {
        int szam = atoi(sor);
        da_append(szamok, szam);
    }
    fclose(in);

    da_sort(szamok, 0, szamok->length - 1);
    da_print(szamok);
    
    da_destroy(szamok);
    
    return 0;
}