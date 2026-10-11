from keres import *

# A tábla: 5×5-ös rács
#   M = {(i,j) | 0≤i,j≤4},  |M| = 25
#
# Mozgásszabályok:
#   - Kék korongok: csak LEFELÉ (↓) vagy JOBBRA (→) léphetnek / ugorhatnak
#   - Piros korongok: csak FELFELÉ (↑) vagy BALRA (←) léphetnek / ugorhatnak
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot a tábla konfigurációja:
#   S = M → {'B','R','0'}   (minden mezőn kék, piros vagy üres)
# Reprezentáció: tuple of tuples (5×5 karakter-rács), hasítható.
#
# KEZDŐÁLLAPOT (képről leolvasva)
# --------------------------------
#   s₀ =   B B B R R
#          B B B R R
#          B B 0 R R
#          B B R R R
#          B B R R R
#
# CÉLÁLLAPOT
# ----------
# s* = a korongok felcserélve:
#   ahol kék volt → piros, ahol piros volt → kék, az üres mező marad.
#
# OPERÁTOROK HALMAZA
# ------------------
# O = { move(korong, irány) | korong ∈ M, irány ∈ {↑,↓,←,→} }
#
# Korong mozgatható, ha:
#   (a) Lépés: a szomszédos mező az irányban üres
#   (b) Ugrás: a szomszéd másik színű korong, és az azon túli mező üres
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Legyen p a korong pozíciója, sz = p + irány, sz2 = p + 2*irány
#
# Lépés:   Pre_lépés(move(p, irány), s) ≡
#               p ∈ M ∧ s[p] ∈ {B,R}
#             ∧ sz ∈ M ∧ s[sz] = '0'
#             ∧ irány ∈ megengedett_irányok(s[p])
#
# Ugrás:   Pre_ugrás(move(p, irány), s) ≡
#               p ∈ M ∧ s[p] ∈ {B,R}
#             ∧ sz ∈ M ∧ s[sz] ∈ {B,R} ∧ s[sz] ≠ s[p]   (másik szín)
#             ∧ sz2 ∈ M ∧ s[sz2] = '0'
#             ∧ irány ∈ megengedett_irányok(s[p])
#
# Megengedett irányok:
#   Kék  (B): {↓, →}  azaz (dr,dc) ∈ {(+1,0),(0,+1)}
#   Piros(R): {↑, ←}  azaz (dr,dc) ∈ {(-1,0),(0,-1)}
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# Lépés:  γ(move(p, irány), s): s[sz] ← s[p], s[p] ← '0'
# Ugrás:  γ(move(p, irány), s): s[sz2] ← s[p], s[p] ← '0'
# =============================================================================

IRÁNYOK = {
    'B': [(1, 0), (0, 1)],   # le, jobbra
    'R': [(-1, 0), (0, -1)], # fel, balra
}

TÁBLA_MÉRET = 5

def index(sor, oszlop):
    return sor * TÁBLA_MÉRET + oszlop


def kis_tábla():
    t = []
    for i in range(3):
        sor = []
        for j in range(3):
            if (i == 1 and j == 1):
                sor.append('0')
            elif (j < 1 or (j == 1 and i < 1)):
                sor.append('B')
            elif (j > 1 or (j == 1 and i > 1)):
                sor.append('R')
        t.append(tuple(sor))
    return tuple(t)

def kezdő_tábla():
    t = []
    for i in range(5):
        sor = []
        for j in range(5):
            if (i == 2 and j == 2):
                sor.append('0')
            elif (j < 2 or (j == 2 and i < 2)):
                sor.append('B')
            elif (j > 2 or (j == 2 and i > 2)):
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
        self.kezdő = kis_tábla()
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
                    # Ugrás: szomszéd másik szín, és azon túl üres
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

    
    kov = feladat.rákövetkező((('B', 'B', 'R'),
                               ('B', '0', 'R'),
                               ('B', 'R', 'R')))
    
    kov = feladat.rákövetkező((('B', 'B', 'B', 'R', 'R'),
                               ('B', 'B', 'R', '0', 'R'),
                               ('B', 'B', 'B', 'R', 'R'),
                               ('B', 'B', 'R', 'R', 'R'),
                               ('B', 'B', 'R', 'R', 'R')))
    for n, t in enumerate(kov):
        print(f"{n+1}. gyerek:  {t}")
        
        tábla_kiír(t[-1])

    """
    kov = feladat.rákövetkező(('B', 'B', 'B', 'R', 'R',
                               'B', 'R', 'B', 'B', 'R',
                               'B', 'B', 'R', 'B', 'R',
                               'B', 'B', 'R', 'R', 'R',
                               'B', 'B', 'R', '0', 'R'))
    for t in kov:
        tábla_kiír2(t[-1])
    """


    #result1 = best_first(feladat, heurisztika)
    #print(f"Best_first:\t\t {result1.megoldás()}")

    #result2 = szélességi_fakereső(feladat)
    #print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

