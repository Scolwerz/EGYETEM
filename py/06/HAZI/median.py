#!/usr/bin/env python3




def main():
    nums = [3, 6, 20, 99, 10, 15]
    sorted_nums = sorted(nums)
    n = len(sorted_numbers)
    
    if n % 2 == 1:  #páratlan elem
        result = sorted_nums[n // 2]
    else:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        result = (mid1 + mid2) / 2

    print(result)
    

################################################################


if __name__ == '__main__':
    main()