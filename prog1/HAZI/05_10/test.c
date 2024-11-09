#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

#define MAX_TANULO 100
#define BUFFER 222
#define MAX 100

typedef char* string;

void uppercase(char* s) {
    int length = strlen(s);
    for (int i = 0; i < length; i++)
    {
        s[i] = toupper(s[i]);
    }
}

void sort(const int n, string s[]) {
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-1-i; j++)
        {
            if (strcmp(s[j], s[j+1]) > 0)
            {
                string tmp = s[j];
                s[j] = s[j+1];
                s[j+1] = tmp;
            }
        }
    }
}


void kiir(const int n, string s[])
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
    string filename = "nevek.csv";
    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFFER];
    char name[100], major[100];
    int age, n = 0;
    string students[MAX];
    while (fgets(line, BUFFER, in) != NULL)
    {
        line[strlen(line) - 1] = '\0';
        char *p = strtok(line, ",");  strcpy(name, p);
        p = strtok(NULL, ",");  //age = atoi(p);
        p = strtok(NULL, ","); //strcpy(major, p);
        if (strcasecmp(p, "PTI") == 0)
        {
            char *name_copy = malloc(strlen(name) + 1);
            strcpy(name_copy, name);
            students[n] = name_copy;
            n++;
        }
    }
    fclose(in);

    sort(n, students);
    kiir(n, students);
    
    //free(name_copy);
    //free(students);

    return 0;
}