#!/usr/bin/env python3

import math


def distance(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    c = math.sqrt(a**2 + b**2)
    return c


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
    