#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

#define BUFFER 222
#define MAX 100

void sort(const int n, char* s[]) {
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-1-i; j++)
        {
            if (strcmp(s[j], s[j+1]) > 0)
            {
                char* tmp = s[j];
                s[j] = s[j+1];
                s[j+1] = tmp;
            }
        }
    }
}

void kiir(const int n, char* s[])
{
    int i;
    for (i = 0; i < n-1; i++)
    {
        printf("%c%s, ", toupper(s[i][0]), &(s[i][1]));
    }
    printf("%c%s\n", toupper(s[i][0]), &(s[i][1]));
}

int main ()
{
    char* filename = "nevek.csv";
    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFFER];
    char name[MAX], major[MAX];
    char* name_copy;
    char* students[MAX];
    int n = 0;
    while (fgets(line, BUFFER, in) != NULL)
    {
        line[strlen(line) - 1] = '\0';
        char *p = strtok(line, ",");  strcpy(name, p);
        p = strtok(NULL, ",");        //int age = atoi(p);
        p = strtok(NULL, ",");        //strcpy(major, p);
        if (strcasecmp(p, "PTI") == 0)
        {
            name_copy = malloc(strlen(name) + 1);
            strcpy(name_copy, name);
            students[n++] = name_copy;
        }
    }
    fclose(in);

    sort(n, students);
    kiir(n, students);
    
    free(name_copy);


    //free(name);
    //free(students);

    return 0;
}