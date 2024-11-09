#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

#define BUFFER 222
#define MAX 100

typedef struct
{
    char name[MAX];
    int age;
    char major[MAX];
} Student;

void print_student(const Student *s) {
    printf("Nev: %s, Kor: %d, Szak: %s\n", s->name, s->age, s->major);
}

int feltolt(const char* filename, const int n, Student students[]) {
    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFFER];
    Student s;
    int i = 0;
    while (fgets(line, BUFFER, in) != NULL)
    {
        line[strlen(line) - 1] = '\0';
        char *p = strtok(line, ","); strcpy(s.name, p);
              p = strtok(NULL, ","); s.age = atoi(p);
              p = strtok(NULL, ","); strcpy(s.major, p);
        students[i] = s[i++];
    }
    fclose(in);

    return i;    
}

int szures(const int n, const Student students[], Student ptisek[]) {
    int i = 0;
    for (int j = 0; j < n; j++)
    {
        Student temp = students[j];
        if (strcasecmp(temp.major, "PTI") == 0)
        {
            ptisek[i++] = students[j];
        }
    }

    return i;
}

void sort(const int n, Student s) {
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-1-i; j++)
        {
            if (strcmp(s[j].nev, s[j+1].nev) > 0)
            {
                Student tmp = s[j];
                s[j] = s[j+1];
                s[j+1] = tmp;
            }
        }
    }
}

void kiir(const int n, char** s) {
    int i;
    for (i = 0; i < n-1; i++)
    {
        printf("%c%s, ", toupper(s[i][0]), &(s[i][1]));
    }
    printf("%c%s\n", toupper(s[i][0]), &(s[i][1]));
}

int cmp_names(const void *a, const  void *b)
{
    return strcmp( *(const Student*)a->name, *(const Student*)b->name);
}

int main ()
{
    const char* filename = "nevek.csv";

    Student students[MAX];
    int n;
    int s_num = feltolt(filename, MAX, students);
    for (int i = 0; i < s_num; i++)
    {
        print_student(&students[i]);
        n++;
    }
    puts("-------------");
    Student students_pti[MAX];
    int pti_num = szures(n, students, students_pti);
    for (int i = 0; i < pti_num; i++)
    {
        print_student(&students_pit[i]);
    }
    
    sort(pti_num, students_pti);


    
    return 0;
}