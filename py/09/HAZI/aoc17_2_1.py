#!/usr/bin/env python3


def checksum(matrix):
    total = 0
    for row in matrix:
        min_val = min(row)
        max_val = max(row)
        total += max_val - min_val
    return total


def main():
    matrix = []
    filename = 'input.txt'
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)

    result = checksum(input_matrix)
    print("A táblázat ellenőrző összege:", result)


#############################################################################

if __name__ == "__main__":
    main()