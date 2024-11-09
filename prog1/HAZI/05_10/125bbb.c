#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#define MAX 100
#define BUFFER 111

typedef struct {
    char name[50];
    int age;
    char major[50];
} Student;

int feltolt(const char* fname, int n, Student students[])
{
    FILE *in = fopen(fname, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error:");
        exit(1);
    }
    
    char line[BUFFER];
    char *p;
    char* name, major;
    int age;
    int index = 0;
    while (fgets(line, BUFFER, in) != NULL)
    {
        line[strlen(line)-1] = '\0';
        
        p = strtok(line, ","); name = p;
        p = strtok(NULL, ","); age = atoi(p);
        p = strtok(NULL, ","); major = p;

        if (strcasecmp(major, "PTI") == 0)
        {
            Student h;
            strcpy(h.name, name);
            h.age = age;
            strcpy(h.major, major);
            students[index++] = h;
        }
    }
    fclose(in);
    
    return index;
}

void print_student(Student *h)
{
    printf(" nev: %s, kor: %d, szak: %s\n", h->name, h->age, h->major);
}


int main()
{
    const char* fname = "nevek.csv";
    Student students[MAX];
    
    int n = feltolt(fname, MAX, students);
    for (int i = 0; i < n; i++)
    {
        print_student(&students[i]);
    }

    return 0;
}