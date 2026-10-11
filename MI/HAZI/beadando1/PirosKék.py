from keres import *

IRÁNYOK = {
    'B': [(1, 0), (0, 1)],   # le, jobbra
    'R': [(-1, 0), (0, -1)], # fel, balra
}

TÁBLA_MÉRET = 5

def index(sor, oszlop):
    return sor * TÁBLA_MÉRET + oszlop

def kezdő_tábla():
    t = []
    FÉL = TÁBLA_MÉRET // 2
    for i in range(TÁBLA_MÉRET):
        sor = []
        for j in range(TÁBLA_MÉRET):
            if (i == FÉL and j == FÉL):
                sor.append('0')
            elif (j < FÉL or (j == FÉL and i < FÉL)):
                sor.append('B')
            elif (j > FÉL or (j == FÉL and i > FÉL)):
                sor.append('R')
        t.append(tuple(sor))
    return tuple(t)

def cél_tábla(kezdő):
    t = []
    for sor in kezdő:
        új_sor = []
        for mező in sor:
            if mező == 'B':
                új_sor.append('R')
            elif mező == 'R':
                új_sor.append('B')
            else:
                új_sor.append('0')
        t.append(tuple(új_sor))
    return tuple(t)

"""
def lépés(állapot, honnan, hova):
    lista_állapot = list(állapot)
    lista_állapot[index(honnan[0],honnan[1])], lista_állapot[index(hova[0],hova[1])] = lista_állapot[index(hova[0],hova[1])], lista_állapot[index(honnan[0],honnan[1])]
    return tuple(lista_állapot)
"""

class PirosKék(Feladat):
    def __init__(self):
        self.kezdő = kezdő_tábla()
        self.cél = cél_tábla(self.kezdő)

    def célteszt(self, a):
        return a == self.cél

    def rákövetkező(self, a):
        gyerekek = []
        
        """
        for i in range(TÁBLA_MÉRET):
            for j in range(TÁBLA_MÉRET):
                szín = a[index(i,j)]
                if (szín == '0'):
                    continue
                if (szín == 'B'):
                    if (j+1 < TÁBLA_MÉRET and a[index(i,j+1)] == '0'):
                        új_állapot = lépés(a, (i,j), (i,j+1))
                        gyerekek.append((f"({i},{j}) Jobbra lép", új_állapot))
                    if (i+1 < TÁBLA_MÉRET and a[index(i+1,j)] == '0'):
                        új_állapot = lépés(a, (i,j), (i+1,j))
                        gyerekek.append((f"({i},{j}) Le lép", új_állapot))
                    if (j+2 < TÁBLA_MÉRET and a[index(i,j+2)] == '0'):
                        új_állapot = lépés(a, (i,j), (i,j+2))
                        gyerekek.append((f"({i},{j}) Jobbra ugrik", új_állapot))
                    if (i+2 < TÁBLA_MÉRET and a[index(i+2,j)] == '0'):
                        új_állapot = lépés(a, (i,j), (i+2,j))
                        gyerekek.append((f"({i},{j}) Le ugrik", új_állapot))
                elif (szín == 'R'):
                    if (j-1 >= 0 and a[index(i,j-1)] == '0'):
                        új_állapot = lépés(a, (i,j), (i,j-1))
                        gyerekek.append((f"({i},{j}) Balra lép", új_állapot))
                    if (i-1 >= 0 and a[index(i-1,j)] == '0'):
                        új_állapot = lépés(a, (i,j), (i-1,j))
                        gyerekek.append((f"({i},{j}) Fel lép", új_állapot))
                    if (j-2 >= 0 and a[index(i,j-2)] == '0'):
                        új_állapot = lépés(a, (i,j), (i,j-2))
                        gyerekek.append((f"({i},{j}) Balra ugrik", új_állapot))
                    if (i-2 >= 0 and a[index(i-2,j)] == '0'):
                        új_állapot = lépés(a, (i,j), (i-2,j))
                        gyerekek.append((f"({i},{j}) Fel ugrik", új_állapot))
        """

        sorhossz = len(a[0])
        for i in range(sorhossz):
            for j in range(sorhossz):
                szín = a[i][j]
                
                if (szín == '0'):
                    continue

                for dsor, doszlop in IRÁNYOK[szín]:
                    új_i, új_j = i + dsor, j + doszlop
                    if (0 <= új_i < sorhossz and 0 <= új_j < sorhossz
                        and a[új_i][új_j] == '0'):
                        lista_állapot = [list(sor) for sor in a]
                        lista_állapot[új_i][új_j] = szín
                        lista_állapot[i][j] = '0'
                        új_állapot = tuple(tuple(s) for s in lista_állapot)
                        gyerekek.append((f"{szín}({i},{j}) -> ({új_i},{új_j})", új_állapot))
                    # Ugrás: szomszéd másik színű, és mögötte üres
                    elif (0 <= új_i < sorhossz and 0 <= új_j < sorhossz
                          and a[új_i][új_j] not in ('0', szín)):
                        ni, nj = i + 2*dsor, j + 2*doszlop
                        if (0 <= ni < sorhossz and 0 <= nj < sorhossz
                            and a[ni][nj] == '0'):
                            lista_állapot = [list(sor) for sor in a]
                            lista_állapot[ni][nj] = szín
                            lista_állapot[i][j] = '0'
                            új_állapot = tuple(tuple(s) for s in lista_állapot)
                            gyerekek.append((f"{szín}({i},{j}) ---> ({ni},{nj})", új_állapot))
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    cél = cél_tábla(kezdő_tábla())
    nincs_helyén = 0
    sorhossz = len(a[0])
    for i in range(sorhossz):
        for j in range(sorhossz):
            if a[i][j] != '0' and a[i][j] != cél[i][j]:
                nincs_helyén = nincs_helyén + 1
    return nincs_helyén

def tábla_kiír(tábla):
    for sor in tábla:
        print(" ".join(m for m in sor))
    print()

"""
def tábla_kiír2(tábla):
    for i in range(0,TÁBLA_MÉRET*TÁBLA_MÉRET,5):
        print(f"{tábla[i+0]} {tábla[i+1]} {tábla[i+2]} {tábla[i+3]} {tábla[i+4]}")
    print()
"""

if __name__ == '__main__':
    feladat = PirosKék()

    print(f"Kezdőállapot:")
    print(feladat.kezdő)
    tábla_kiír(feladat.kezdő)
    

    print(f"Célállapot:")
    print(feladat.cél)
    tábla_kiír(feladat.cél)

    #kov = feladat.rákövetkező((('B', 'B', 'R'),
    #                           ('B', '0', 'R'),
    #                           ('B', 'R', 'R')))
    #
    #kov = feladat.rákövetkező((('B', 'B', 'B', 'R', 'R'),
    #                           ('B', 'B', 'R', '0', 'R'),
    #                           ('B', 'B', 'B', 'R', 'R'),
    #                           ('B', 'B', 'R', 'R', 'R'),
    #                           ('B', 'B', 'R', 'R', 'R')))
    #for n, t in enumerate(kov):
    #    print(f"{n+1}. gyerek:  {t}")
    #    tábla_kiír(t[-1])

    """
    kov = feladat.rákövetkező(('B', 'B', 'B', 'R', 'R',
                               'B', 'R', 'B', 'B', 'R',
                               'B', 'B', 'R', 'B', 'R',
                               'B', 'B', 'R', 'R', 'R',
                               'B', 'B', 'R', '0', 'R'))
    for t in kov:
        tábla_kiír2(t[-1])
    """

    result1 = best_first(feladat, heurisztika)
    print(f"Best_first:\t\t {result1.megoldás()}")

    result2 = szélességi_fakereső(feladat)
    print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

