/* Bővítse ki az előadáson látott dinamikus tömb implementációját egy
   void da_clear(DynArray *self); szignatúrájú eljárással. Az eljárás
   törölje ki a dinamikus tömbben tárolt összes elemet. Figyeljen arra is,
   hogy ne lépjen fel memóriaszivárgás! Ennek ellenőrzésére használja a
   valgrind eszközt. Az elemek törlése után a dinamikus tömbbe természetesen
   ismét lehessen elemeket beszúrni (ezt is próbálja ki). */
#include <stdio.h>
#include <stdlib.h>

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

void da_clear(DynArray *self) {
    self->length = 0;
    self->elems = realloc(self->elems, INITIAL_CAPACITY * sizeof(int));
    if (self->elems == NULL)
    {
        mem_error();
    }
    self->capacity = INITIAL_CAPACITY;
}

void da_print(DynArray *self) {
    for (int i = 0; i < self->length; i++)
    {
        printf("%d ", self->elems[i]);
    }
}

int main()
{
    DynArray *szamok = da_create();

    for (int i = 1; i <= 100; i++)
    {
        da_append(szamok, i);
    }
    puts("Elotte: ");
    da_print(szamok);
    puts("");
    da_clear(szamok);

    for (int i = 1; i <= 10; i++)
    {
        da_append(szamok, i);
    }
    puts("Utana: ");
    da_print(szamok);
    puts("");

    da_destroy(szamok);

    return 0;
}