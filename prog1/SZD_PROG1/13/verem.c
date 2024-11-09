#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// A fej mutatja a verem tetejét

typedef struct listaelem
{
    int data
    struct listaelem *next;    
} LISTAELEM;

LISTAELEM *head = NULL;

bool empty()
{
    return heead == 0;
}

void push(int data)
{
    LISTAELEM *new = malloc(sizeof(LISTAELEM));
    new->data = data;
    new->next = head;
    head = new
}

int pop()
{
    if (ures())
    {
        printf("Error: üres verem");
    }
    else
    {
        int result = head->data;

        LISTAELEM *tmp = head->next;
        free(head);
        head = tmp;

        return ertek;
    }
}

void bejar()
{
    LISTAELEM *current = head;
    while (current != NULL)
    {
        printf("%d", current->data);
        current = current->next;
    }
}

int main()
{


    return 0;
}