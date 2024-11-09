
char* get_string(const char* prompt) {
    char text[1024];
    printf("%s", prompt);
    fgets(text, sizeof(text), stdin);
    text[strlen(text) - 1] = '\0';
    return strdup(text);
}

int get_int(const char* prompt) {
    int x;
    printf("%s", s);
    scanf("%d", &x);
    return x;
}

int get_random(int intmin, int intmax) {
    return rand() % (intmax - intmin + 1) + intmin;
}

void print_array(const int n, int t[]) {
    for (int i=0; i<n; i++)
    {
        printf("%d ", t[i]);
    }
    puts("");
}

void print_matrix(int n, int m, int matrix[n][m]) {
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d\t", matric[i][j]);
        }
        puts("");
    }
}

void my_strfry(char *s) {
    int length = strlen(s);
    for (int i = 0; i < length - 1; i++)
    {
        int range = length -i;
        int j = i + rand() % range;
        swap(&s[i], &s[j]);
    }
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

SORT ALGS. {
void bubblesort(const int n, int t[]) {
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (t[j] > t[j+1])
            {
                swap(&t[j], &t[j+1]);
            }
        }
    }
}  

void quicksort(int t[], const int bal, const int jobb) {
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

}

TÖMBSTATISZTIKA {
typedef struct arraystats {
    int min, max;
    double avg;
} Stats;

Stats arraystats(const int n, int t[]) {
    Stats x;
    x.min = x.max = t[0];
    for (int i=0; i<n; i++)
    {
        x.min = t[i] < x.min ? t[i] : x.min;
        x.max = t[i] > x.max ? t[i] : x.max;
        x.avg += t[i];
    }
    x.avg /= n;
    return x;
}

}

FÁJLKEZELÉS {
    
int num_lines(const char* filename) {
    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }
    int counter = 0;
    char line[BUFFER];
    while (fgets(line, BUFFER, in) != NULL)
    {
        coubnter++;
    }
    fclose(in);
}
    
int * read_ints(const char* filename, int num_lines) {
    int *t = malloc(num_lines * sizeof(int));
    int i = 0;

    FILE *in = fopen(filename, "r");
    if (in == NULL)
    {
        fprintf(stderr, "Error: cannot open %s\n", filename);
        exit(1);
    }

    char line[BUFFER];
    while (fgets(line, BUFFER, in) != NULL)
    {
        t[i] = atoi(line);
        i++;
    }
    fclose(in);
    
    return t;
}

}

DINAMIKUS TÖMB {
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
    self->elems = realloc(self->elems, INITIAL_CAPACITY * sizeof(int));
    self->length = 0;
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

void da_bublesort(DynArray *self) {
    for (int i = 0; i < self->length - 1; i++)
    {
        for (int j = 0; j < self->length - i - 1; j++)
        {
            if (self->elems[j] > self->elems[j+1])
            {
                swap(&self->elems[j], &self->elems[j+1]);
            }
        }
    }
}

void da_quicksort(DynArray *self, const int bal, const int jobb) {
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

double da_average(const DynArray *self) {
    return ((double)da_sum(self) / (double)self->length);
}

int da_sum(const DynArray *self) {
    int sum = 0;
    for (int i = 0; i < self->length; i++)
    {
        sum += self->elems[i];
    }
    return sum;
}

}

STRING TOKENIZACIO {
    char line[] = {a bb cc};
    char *p;
    
    p = strtok(line, " ");
    while (p != NULL)
    {
        printf("%s\n", p);
        p = strtok(NULL, " ");
    }
}








https://manual.cs50.io/

stringek: https://www.youtube.com/watch?v=1TE4-Qi2y4c
https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=C.20150317c