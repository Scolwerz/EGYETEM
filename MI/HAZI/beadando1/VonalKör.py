from keres import *

"""
RÁCSMÉRET = 8
ÖSSZES_MEZŐ = RÁCSMÉRET * RÁCSMÉRET  # 64

PONTOK = {
    (0, 0), (0, 4),
    (1, 3), (1, 6),
    (2, 2),
    (3, 5),
    (4, 1), (4, 4),
    (5, 2), (5, 7),
    (6, 0), (6, 5),
    (7, 3), (7, 7)
} # nincs megoldás
"""

RÁCSMÉRET = 4
ÖSSZES_MEZŐ = RÁCSMÉRET * RÁCSMÉRET  # 16
PONTOK = {
    (0,0), (0,3),
    (1,1), (1,2),

    (3,0), (3,1), (3,2), (3,3)
}

START = (0, 0)

def szomszédos_mezők(mező):
    sor, oszlop = mező
    szomszédok = []
    if sor > 0:                 szomszédok.append((sor - 1, oszlop))
    if sor < RÁCSMÉRET - 1:     szomszédok.append((sor + 1, oszlop))
    if oszlop > 0:              szomszédok.append((sor, oszlop - 1))
    if oszlop < RÁCSMÉRET - 1:  szomszédok.append((sor, oszlop + 1))
    return szomszédok

def irány(honnan, hova):
    return (hova[0] - honnan[0], hova[1] - honnan[1])

def skalárszorzat(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def irány_helyes(útvonal, következő):
    if len(útvonal) < 2: # első lépés
        return True
    
    aktuális = útvonal[-1]
    előző = útvonal[-2]
    bejövő = irány(előző, aktuális)
    kimenő = irány(aktuális, következő)
    if aktuális in PONTOK:
        return (skalárszorzat(bejövő, kimenő) == 0) #merőleges
    else:
        return (skalárszorzat(bejövő, kimenő) > 0) #megegyező


class VonalKör(Feladat):
    def __init__(self):
        self.kezdő = (START, )
        self.cél = None

    def célteszt(self, a):
        if len(a) != ÖSSZES_MEZŐ:
            return False

        utolsó = a[-1]
        első = a[0]
        különbség = (utolsó[0] - első[0], utolsó[1] - első[1])
        if különbség not in [(1,0), (0, 1), (-1, 0),(0, -1)]:
            return False

        if not irány_helyes(a, első):
            return False
        
        if első in PONTOK:
            nyitó = irány(a[0], a[1])
            záró = irány(a[-1],a[0])
            return (skalárszorzat(záró, nyitó) == 0)
        return True

    def rákövetkező(self, a):
        aktuális = a[-1]
        gyerekek = []
        for szomszéd in szomszédos_mezők(aktuális):
            if szomszéd in a:
                continue
            if not irány_helyes(a, szomszéd):
                continue
            új_állapot = a + (szomszéd,)
            gyerekek.append((f"{aktuális}->{szomszéd}", új_állapot))

        return gyerekek


def heurisztika(csúcs):
    állapot = csúcs.állapot
    meglátogatott = len(állapot)
    összes = RÁCSMÉRET * RÁCSMÉRET
    return összes - meglátogatott


if __name__ == '__main__':
    feladat = VonalKör()

    #kov = feladat.rákövetkező(((0,2),))
    #
    #for n, t in enumerate(kov):
    #    print(f"{n+1}. gyerek:  {t}")
    #    print()

    result1 = best_first(feladat, heurisztika)
    print(f"Best_first:\t\t {result1.megoldás()}")

    result2 = szélességi_fakereső(feladat)
    print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

