#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

int get_random(int intmin, int intmax)
{
    return rand() % (intmax-intmin+1) + intmin;
}

int main()
{
    srand(time(NULL));
    
    char special[] = {'.', ',', ';', '\''};
    int n_special = sizeof(special) / sizeof(special[0]);
    
    int min_len = 8, max_len = 12, pw_len;
    char pw[max_len + 1];
    int category, prev_category = -1;
    int has_lower = 0, has_upper = 0, has_number = 0, has_special = 0;
    int i;
    
    do
    {
        pw_len = get_random(min_len, max_len);
        for (i = 0; i < pw_len; i++)
        {
            while (category == prev_category)
            {
                category = get_random(0,3);
            }
            switch (category)
            {
                case 0: pw[i] = 'a' + get_random(0,25); has_lower = 1; break;
                case 1: pw[i] = 'A' + get_random(0,25); has_upper = 1; break;
                case 2: pw[i] = '0' + get_random(0,9); has_number = 1; break;
                case 3: pw[i] = special[get_random(0,n_special-1)]; has_special = 1; break;
            }
            prev_category = category;
        }
        pw[i] = '\0';
    } while (!(pw_len >= min_len && pw_len <= max_len &&
               has_lower && has_upper && has_number && has_special) );
    
    printf("Generalt jelszo: %s\n", pw);
    
    return 0;
}