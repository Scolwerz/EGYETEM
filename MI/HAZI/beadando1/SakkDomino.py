from keres import *

TÁBLA_MÉRET = 5
ÖSSZES_MEZŐ = TÁBLA_MÉRET * TÁBLA_MÉRET

def index(sor, oszlop):
    return sor * TÁBLA_MÉRET + oszlop

def coordinate(idx):
    sor = idx // TÁBLA_MÉRET
    oszlop = idx % TÁBLA_MÉRET
    return (sor, oszlop)

def dominó_lerak(állapot, dominó):
    lista_állapot = list(állapot)
    for dsor, doszlop in dominó:
        lista_állapot[index(dsor, doszlop)] = True
    return tuple(lista_állapot)


def első_szabad(állapot, kezdősor=0, kezdőoszlop=0):
    for sor in range(kezdősor, TÁBLA_MÉRET):
        for oszlop in range(kezdőoszlop, TÁBLA_MÉRET):
            #print(f"{sor = } {oszlop = }   {állapot[index(sor, oszlop)]}")
            if (állapot[index(sor, oszlop)] == False):
                return (sor, oszlop)
    return None

def lerakható_v(állapot, sor, oszlop):
    if (oszlop+2 < TÁBLA_MÉRET and
        állapot[index(sor, oszlop)] == False and
        állapot[index(sor, oszlop+1)] == False and
        állapot[index(sor, oszlop+2)] == False):
        return [(sor, oszlop), (sor, oszlop+1), (sor, oszlop+2)]
    return None

def lerakható_f(állapot, sor, oszlop):
    if (sor+2 < TÁBLA_MÉRET and
        állapot[index(sor, oszlop)] == False and
        állapot[index(sor+1, oszlop)] == False and
        állapot[index(sor+2, oszlop)] == False):
        return [(sor, oszlop), (sor+1, oszlop), (sor+2, oszlop)]
    return None


class SakkDomino(Feladat):
    def __init__(self):
        self.kezdő = tuple(False for _ in range(ÖSSZES_MEZŐ))
        self.cél = None

    def célteszt(self, a):
        return a.count(False) == 1

    def rákövetkező(self, a):
        gyerekek = []
       
        szabad = None
        sor, oszlop = 0, 0
        while (sor < TÁBLA_MÉRET and oszlop < TÁBLA_MÉRET):
            szabad = első_szabad(a,sor,oszlop)
            if (szabad is None):
                break
            sor, oszlop = szabad

            dominó_v = lerakható_v(a, sor, oszlop)
            dominó_f = lerakható_f(a, sor, oszlop)
            if (dominó_v is not None):
                #print("\tGYEREK APPEND VSZ")
                új_állapot = dominó_lerak(a, dominó_v)
                gyerekek.append((f"lerak{dominó_v}", új_állapot))
            if (dominó_f is not None):
                #print("\tGYEREK APPEND FÜG")
                új_állapot = dominó_lerak(a, dominó_f)
                gyerekek.append((f"lerak{dominó_f}", új_állapot))
            
            sor, oszlop = coordinate(index(sor,oszlop)+1)

        return gyerekek

def heurisztika(csúcs):
    return (ÖSSZES_MEZŐ - len(csúcs.állapot)) // 3

if __name__ == '__main__':
    feladat = SakkDomino()

    #kezdo = tuple(False for _ in range(ÖSSZES_MEZŐ))
    kezdo = (True, True, True, True, True, True, True, True,
             False, True, False, True, False, False, True, True,
             True, False, False, True, False, False, False, True,
             False, False, True, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False
             )
    #kov = feladat.rákövetkező(kezdo)

    result2 = szélességi_fakereső(feladat)
    print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

    result5 = best_first(feladat, heurisztika)
    print(f"best_first:\t\t {result5.megoldás()}")
