#!/usr/bin/env python3


def main():
    n = 2 ** 1000
    digits = [int(c) for c in str(n)]
    sum_of_digits = sum(digits)

    print("A 2^1000 számjegyeinek összege:", sum_of_digits)


################################################################


if __name__ == '__main__':
    main()

