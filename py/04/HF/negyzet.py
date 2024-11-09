#!/usr/bin/env python3


def osszegnegyzet(li):
    ossezg = 0
    for n in li:
        osszeg += n
    return osszeg**2


def negyzetosszeg(li):
    osszeg = 0
    for n in li:
        osszeg += n**2
    return osszeg


def main():
    szamok = list(range(10+1))
    negyzetosszeg = negyzetosszeg(szamok)
    osszegnegyzet = osszegnegyzet(szamok)
    result = osszegnegyzet - negyzetosszeg
    print(str(result))

#############################################################################

if __name__ == "__main__":
    main()
