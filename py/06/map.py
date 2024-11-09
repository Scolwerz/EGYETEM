#!/usr/bin/env python3


def main():
    d = {}
    d['a'] = "ALFA"
    d['b'] = "BETA"
    d['g'] = "gamma"
    d['a'] = "alfa"
    d['o'] = "omega"
    d['d'] = "delta"
    print(d)

    
    for k in sorted(d.keys()): #d.keys() == d
        print(k,"->",d[k])
    print("-"*30)
    for k,v in d.items():
        print(k,"->",v)

    del d['g']
    print(d)

#############################################################################

if __name__ == "__main__":
    main()
