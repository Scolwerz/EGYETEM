#!/usr/bin/env python3


def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = range(ord('a'), ord('z') + 1)

    for char, code in zip(chars, codes):
        print((char, code))

#############################################################################

if __name__ == "__main__":
    main()