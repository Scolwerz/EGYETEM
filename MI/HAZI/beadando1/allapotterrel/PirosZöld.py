from keres import *

SOROK = 5
OSZLOPOK = 3

KEZDŐ = (
    ('G','G','G'),
    (-1,None,-1),
    (None, None, -1),
    (-1, None, -1),
    ('R','R','R')
)

def cél_tábla(kezdő):
    új_tábla = []
    for sor in KEZDŐ:
        új_sor = []
        for elem in sor:
            if elem == 'G':
                új_sor.append('R')
            elif elem == 'R':
                új_sor.append('G')
            else:
                új_sor.append(elem)
        új_tábla.append(tuple(új_sor))
    return tuple(új_tábla)


def szomszédos_mezők(sor, oszlop):
    szomszédok = []
    if sor > 0:                 szomszédok.append((sor - 1, oszlop))
    if sor < SOROK - 1:         szomszédok.append((sor + 1, oszlop))
    if oszlop > 0:              szomszédok.append((sor, oszlop - 1))
    if oszlop < OSZLOPOK - 1:   szomszédok.append((sor, oszlop + 1))
    return szomszédok


class PirosZöld(Feladat):
    def __init__(self):
        self.kezdő = KEZDŐ
        self.cél = cél_tábla(self.kezdő)

    def célteszt(self, a):
        return a == self.cél

    def rákövetkező(self, a):
        gyerekek = []
        
        sorhossz = len(a)
        oszlophossz = len(a[0])
        for i in range(sorhossz):
            for j in range(oszlophossz):
                szín = a[i][j]
                
                if (szín in (-1, None)):
                    continue

                for szomszéd in szomszédos_mezők(i,j):
                    új_i, új_j = szomszéd
                    if a[új_i][új_j] is None:
                        lista_állapot = [list(sor) for sor in a]
                        lista_állapot[új_i][új_j], lista_állapot[i][j] = lista_állapot[i][j], lista_állapot[új_i][új_j]
                        új_állapot = tuple(tuple(s) for s in lista_állapot)
                        gyerekek.append((f"{szín}({i},{j}) -> ({új_i},{új_j})", új_állapot))
    
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    cél = cél_tábla(KEZDŐ)
    nincs_helyén = 0
    sorhossz = len(a)
    oszlophossz = len(a[0])
    for i in range(sorhossz):
        for j in range(oszlophossz):
            if a[i][j] != '0' and a[i][j] != cél[i][j]:
                nincs_helyén = nincs_helyén + 1
    return nincs_helyén


def tábla_kiír(tábla):
    for sor in tábla:
        print(" ".join(str(m) for m in sor))
    print()


if __name__ == '__main__':
    feladat = PirosZöld()

    print(f"Kezdőállapot:")
    print(feladat.kezdő)
    tábla_kiír(feladat.kezdő)
    

    print(f"Célállapot:")
    print(feladat.cél)
    tábla_kiír(feladat.cél)

    
    kov = feladat.rákövetkező((
                            ('G','G','G'),
                            (-1,None,-1),
                            (None, 'R', -1),
                            (-1, None, -1),
                            ('R',None,'R')
                        ))
    for n, t in enumerate(kov):
        print(f"{n+1}. gyerek:  {t}")
        tábla_kiír(t[-1])


    result1 = best_first(feladat, heurisztika)
    print(f"Best_first:\t\t {result1.megoldás()}")

    #result2 = szélességi_fakereső(feladat)
    #print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    #result3 = mélységi_gráfkereső(feladat)
    #print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")
