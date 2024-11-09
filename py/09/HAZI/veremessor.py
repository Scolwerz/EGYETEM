#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.adatok = []

    def ures(self):
        return len(self.adatok) == 0

    def betesz(self, elem):
        self.adatok.append(elem)

    def kivesz(self):
        if self.ures():
            return None
        return self.adatok.pop()

    def meret(self):
        return len(self.adatok)

    def __str__(self):
        return '[' + ' '.join(str(elem) for elem in self.adatok)


class Sor:
    def __init__(self):
        self.adatok = []

    def ures(self):
        return len(self.adatok) == 0

    def betesz(self, elem):
        self.adatok.insert(0, elem)

    def kivesz(self):
        if self.ures():
            return None
        return self.adatok.pop()

    def meret(self):
        return len(self.adatok)

    def __str__(self):
        return '[' + ' '.join(str(elem) for elem in self.adatok) + ']'


def main():
    # Verem tesztelés
    v = Verem()
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

    # Sor tesztelés
    s = Sor()
    print(s)         # []
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # [5 4 1]
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # [5 4]
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres sortból akarunk kivenni)


#############################################################################

if __name__ == "__main__":
    main()