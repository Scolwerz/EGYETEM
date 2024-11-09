#!/usr/bin/env python3

import sys


def main():
    """
    f = open('test.txt', 'r')
    
    for line in f:
        line = line.rstrip('\n')
        if line.endswith('.'):
            print(line)

            
    sorok = f.readlines()
    print(sorok)

    
    content = f.read()
    print("'"+content+"'")
    sorok = content.splitlines()
    print(sorok)

    f.close()
    """


    """
    f = open('out.txt', 'w')

    print('Mondom:')
    print('Hello', file=f)
    print(3,True,'asd',4.221,file=f)
    f.write('vala')
    f.write('mi')
    print('Hiba: rossz parameter', file=sys.stderr)

    f.close()
    """

    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            to.write(line)



#############################################################################


if __name__ == '__main__':
    main()
