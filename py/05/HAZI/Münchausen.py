#!/usr/bin/env python3


def muenchausen_number(num):
    powers = [0, 1, 2**2, 3**3, 4**4, 5**5, 6**6, 7**7, 8**8, 9**9]
    num_sum = sum(int(digit) for digit in str(num))
    if num_sum > num:
        return False
    return num == sum(powers[int(digit)] for digit in str(num))
    
def main():
    print("\nFeladat #2:")
    muenchausen_numbers = [num for num in range(440_000_000) if muenchausen_number(num)]
    print(muenchausen_numbers)
    

#############################################################################

if __name__ == "__main__":
    main()