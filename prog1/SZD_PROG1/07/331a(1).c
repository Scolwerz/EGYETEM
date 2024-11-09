#include <stdio.h>
#include <stdlib.h>

/*
void get_first_two_primes(int *p1, int *p2)
{
    *p1 = 2;
    *p2 = 3;    
}
void get_first_two_primes_array(int t[])
{
    t[0]=2;
    t[2]=3;
}
*/

typedef struct
{
    int x,y;
} PairIntInt;

PairIntInt get_first_two_primes()
{
    PairIntInt pair = {2,3};
    // pair.x = 2;
    // pair.y = 3;

    return pair;
}

int main()
{
    /*
    int x,y;

    get_first_two_primes(&x, &y);
    printf("x: %d\ny: %d\n", x, y);
    
    int first_two_primes_t[2];
    get_first_two_primes_array(first_two_primes_t);
    printf("1.: %d\n2.: \n", first_two_primes_t[0], first_two_primes_t[1]);
    */

   PairIntInt result = get_first_two_primes();
   printf("1.: %d\n2.: %d\n", result.x, result.y);
   
   return 0;
}