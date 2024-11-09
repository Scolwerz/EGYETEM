#!/usr/bin/env python3


def main():
    with open('string1.py', 'r') as f, open('stripedstring1.txt','w') as to:
        for line in f:
            if not line.strip().startswith('#'):
                for c in line:
                    if c == '#':
                        to.write('\n')
                        break
                    to.write(c)
                    
    """
    with open('string1.py', 'r') as f, open('stripedstring1.txt','w') as to:
            for line in f:
                if not line.strip().startswith('#'):
                    to.write(line)
    """

#############################################################################


if __name__ == '__main__':
    main()
