#!/usr/bin/env python3


def draw_chessboard(queens):
    n = len(queens)

    print("+-----------------+")
    for row in range(n):
        line = "| "
        for col in range(n):

            if queens[col] == row:
                line += "Q "
            else:
                line += ". "
        line += "|"
        print(line)
    print("+-----------------+")


def main():
    queens = [0, 4, 7, 5, 2, 6, 1, 3]
    draw_chessboard(queens)


################################################################


if __name__ == '__main__':
    main()