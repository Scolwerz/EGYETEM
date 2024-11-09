#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_help()
{
    printf("Usage: alap <template_id>\n");
    printf("\nAvailable options:\n");
    printf("-h\t\tshow this help\n");
    printf("-v\t\tversion info\n");
    printf("--stdout\tdon't create source file, print result to stdout\n");
    printf("\nAvailable templates:\n");
    printf("* c\t\t- C source code [main.c]\n");
    printf("* java\t\t- Java source code [Main.java]\n");
    printf("* py\t\t- Python 3 source code [main.py]\n");
}

void create_c_file(int to_stdout)
{
    if (to_stdout == 1)
    {
        printf("#include <stdio.h>\n\n");
        printf("int main()\n");
        printf("{\n");
        printf("\tprintf(\"Hello!\");");
        printf("\n\treturn 0\n");
        printf("}\n");
    }
    else
    {
        FILE *file = fopen("main.c", "w");
        if (file != NULL)
        {
            fclose(file);
            fprintf(stderr, "error: 'main.c' already exists\n");
            exit(1);
        }
        fprintf(file, "#include <stdio.h>\n\n");
        fprintf(file, "int main()\n");
        fprintf(file, "{\n");
        fprintf(file, "\tprintf(\"Hello!\");");
        fprintf(file, "\n\treturn 0\n");
        fprintf(file, "}\n");

        fclose(file);
        printf("C source code [main.c] created\n");
    }
}

void create_java_file(int to_stdout)
{
    if (to_stdout == 1)
    {
        printf("public class Main\n");
        printf("{\n");
        printf("\tpublic static void main(String[] args)\n");
        printf("\t{\n");
        printf("\t\tSystem.out.println(\"asd\");\n");
        printf("\t}\n");
        printf("}\n");
    }
    else
    {
        FILE *file = fopen("Main.java", "w");
        if (file != NULL)
        {
            fclose(file);
            fprintf(stderr, "error: 'Main.java' already exists\n");
            exit(1);
        }
        fprintf(file, "public class Main\n");
        fprintf(file, "{\n");
        fprintf(file, "\tpublic static void main(String[] args)\n");
        fprintf(file, "\t{\n");
        fprintf(file, "\t\tSystem.out.println(\"asd\");\n");
        fprintf(file, "\t}\n");
        fprintf(file, "}\n");

        fclose(file);
        printf("Java source code [Main.java] created\n");
    }
}

void create_py_file(int to_stdout)
{
    if (to_stdout == 1)
    {
        printf("def main():\n");
        printf("\tprint(\"Py3\")\n");
        printf("\n####################\n");
        printf("\nif __name__ == \"__main__\":\n");
        printf("\tmain()\n");
    }
    else
    {
        FILE *file = fopen("main.py", "w");
        if (file != NULL)
        {
            fclose(file);
            fprintf(stderr, "error: 'main.py' already exists\n");
            exit(1);
        }
        fprintf(file, "def main():\n");
        fprintf(file, "\tprint(\"Py3\")\n");
        fprintf(file, "\n####################\n");
        fprintf(file, "\nif __name__ == \"__main__\":\n");
        fprintf(file, "\tmain()\n");

        fclose(file);
        printf("Python source code [main.py] created\n");
    }
}

int main(int argc, char* argv[])
{

    if (argc == 1)
    {
        print_help();
        return 1;
    }

    int to_stdout = 0;
    if (argc == 3 && strcmp(argv[2], "--stdout") == 0)
    {
        to_stdout = 1;
    }

    if (strcmp(argv[1], "-h") == 0)
    {
        print_help();
        return 0;
    }
    else if (strcmp(argv[1], "-v") == 0)
    {
        printf("alap version: 1.0\n");
        return 0;
    }
    else if (strcmp(argv[1], "c") == 0)
    {
        create_c_file(to_stdout);
    }
    else if (strcmp(argv[1], "java") == 0)
    {
        create_java_file(to_stdout);
    }
    else if (strcmp(argv[1],"py") == 0)
    {
        create_py_file(to_stdout);
    }
    else
    {
        printf("error: invalid template_id: %s\n\n", argv[1]);
        print_help();
        return 1;
    }

    return 0;
}