#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int is_valid(int nums[6])
{
    int sum = 0, prod = 1;
    for (int i = 0; i < 6; i++)
    {
        sum += nums[i];
        prod *= nums[i];
    }
    if (sum != 90 || prod != 996300)
    {
        return 0;
    }
    return 1;
}

void find_numbers(int nums[6], int start, int end, int k, int index)
{
    if (index == 6)
    {
        if (is_valid(nums))
        {
            for (int i = 0; i < 6; i++)
            {
                printf("%d ", nums[i]);
            }
            printf("\n");
        }
        return;
    }
    for (int i = start; i <= end && end - i + 1 >= k - index; i++)
    {
        nums[index] = i;
        find_numbers(nums, i + 1, end, k, index + 1);
    }
}

int main()
{
    int nums[6];

    find_numbers(nums, 1, 45, 6, 0);

    return 0;
}