#!/usr/bin/env python3


def main():
    result = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    print(result)
    

#############################################################################

if __name__ == "__main__":
    main()






