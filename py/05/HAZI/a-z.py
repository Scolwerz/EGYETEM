#!/usr/bin/env python3


import sys


def generate_alphabet(reverse=False):
    """
    Cisszaadja az abc kisbezűit a-z-ig, a reverse paramézerrel z-a-ig
    """
    if reverse:
        return ''.join(chr(122 - i) for i in range(26))
    else:
        return ''.join(chr(97 + i) for i in range(26))


def main():
    reverse = False
    if sys.argv[0] == "./z-a.py":
        reverse = True
    
    alphabet = generate_alphabet(reverse)
    print(alphabet)


#############################################################################

if __name__ == "__main__":
    main()