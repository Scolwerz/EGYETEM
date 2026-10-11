from keres import *

# =============================================================================
# MATEMATIKAI-LOGIKAI ÉS HALMAZELMÉLETI LEÍRÁS – SAKK-DOMINÓ
# =============================================================================
#
# A tábla: szabályos 8×8-as sakktábla
#   M = {(i,j) | 0≤i,j≤7},  |M| = 64 mező
#
# Egy 3×1-es dominó: három egymás melletti mező vízszintesen vagy függőlegesen.
#   Vízszintes: D = [(i,j),(i,j+1),(i,j+2)]
#   Függőleges: D = [(i,j),(i+1,j),(i+2,j)]
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot: 64 elemű bool-tuple, ahol az idx = sor*8 + oszlop indexű
# elem True, ha az (sor, oszlop) mező már le van fedve.
#   S ⊆ {True, False}^64
#
# KEZDŐÁLLAPOT
# ------------
# s₀ = (False, False, ..., False)   – üres tábla, semmi nincs lefedve
#
# CÉLÁLLAPOT
# ----------
# s* olyan bool-tuple, amelyre pontosan 1 elem False:
#   |{ k | s*[k] = False }| = 1
#
# OPERÁTOROK HALMAZA
# ------------------
# O = { place(D) | D érvényes 3×1-es dominó elhelyezés M-en }
# ahol D = [m₁, m₂, m₃] rendezett lista, mᵢ = (sorᵢ, oszlopᵢ)
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Pre(place(D), s) ≡
#     D ⊆ M                         (a dominó a táblán belül van)
#   ∧ ∀ m ∈ D : s[index(m)] = False  (mindhárom mező szabad)
#   ∧ D[0] = első_szabad(s)          (bal-fentről az első szabad mezőre tesszük,
#                                     ezzel elkerüljük a duplikált állapotokat)
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# γ(place(D), s) = s', ahol:
#   s'[index(m)] = True   ha m ∈ D
#   s'[k]        = s[k]   egyébként
#
# MEGJEGYZÉS
# ----------
# A "D[0] = első_szabad(s)" feltétel kulcsfontosságú: mindig a bal-fentről
# első szabad mezőt fedjük le valamelyik dominóval. Ez a szimmetria-törés
# drastikusan csökkenti a keresési teret, és garantálja, hogy minden
# lefedést pontosan egyszer találjuk meg.
# =============================================================================


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

def dominó_heurisztika(csúcs):
    return (ÖSSZES_MEZŐ - len(csúcs.állapot)) // 3

if __name__ == '__main__':
    feladat = SakkDomino()

    #kezdo = tuple(False for _ in range(ÖSSZES_MEZŐ))
    kezdo = (True, True, True, True, True, True, True, True,
             False, False, False, True, False, False, False, True,
             False, False, False, True, False, False, False, True,
             False, False, False, False, False, False, False, False,
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

    result5 = a_csillag(feladat, dominó_heurisztika)
    print(f"a_csillag:\t\t {result5.megoldás()}")
