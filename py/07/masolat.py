#!/usr/bin/env python3

"""
with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            to.write(line)
"""

import shutil


INPUT = "input.txt"
OUTPUT = "output.txt"


def main():
    f = open(INPUT, 'r')
    to = open(OUTPUT, 'w')
    for line in f:
        to.write(line)

    f.close()
    to.close()

    # shutil.copy(f,to)

    
#############################################################################


if __name__ == '__main__':
    main()
