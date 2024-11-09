#!/usr/bin/env python3


def main():
    kosar = ["alma","ananasz","banan","alma","narancs","banan"]
    print(kosar)
    gyumolcs = set(kosar)
    print("A ",gyumolcs)
    #print("ananasz" in gyumolcs)
    #print("kiwi" in gyumolcs)
    print("-"*66)
    b = set()
    b.add("alma")
    b.add("citrom")
    print("B ",b)
    print("-"*66)
    print("a U b ",gyumolcs.union(b))
    print("a - b ", gyumolcs.difference(b))


#############################################################################

if __name__ == "__main__":
    main()
