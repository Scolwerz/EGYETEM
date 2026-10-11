from keres import *

# =============================================================================
# MATEMATIKAI-LOGIKAI ÉS HALMAZELMÉLETI LEÍRÁS – HÁROMSZÖG-TOLOGATÓS (LISTÁVAL)
# =============================================================================
#
# A TÁBLA STRUKTÚRÁJA
# -------------------
# Egy n=4 sorból álló háromszög, ahol az i-edik sor (0-tól indexelve)
# (2i+1) kis háromszöget tartalmaz.
#   Sor 0: 1 háromszög
#   Sor 1: 3 háromszög
#   Sor 2: 5 háromszög
#   Sor 3: 7 háromszög
#   Összesen: 16 cella
#
# HÁROMSZÖG TÍPUSA
# ----------------
# Minden cella (sor, poz) kétféle lehet:
#   ▲ FELFELÉ MUTATÓ  ↔  poz páros  (poz % 2 == 0)
#   ▽ LEFELÉ MUTATÓ   ↔  poz páratlan (poz % 2 == 1)
#
# SZOMSZÉDSÁGI RELÁCIÓ
# --------------------
# Egy (sor, poz) cella szomszédai:
#   1. Vízszintes bal:  (sor, poz-1)   ha poz > 0
#   2. Vízszintes jobb: (sor, poz+1)   ha poz < 2*sor
#   3. Átlós:
#      Ha ▲ (poz páros):  lefelé → (sor+1, poz+1)   ha sor < 3
#      Ha ▽ (poz páratlan): felfelé → (sor-1, poz-1) ha sor > 0
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot: soronkénti tuple-ok tuple-je (hasítható, gráfkeresőbe tehető):
#
#   s = ( (sor0_elem0,),
#         (sor1_elem0, sor1_elem1, sor1_elem2),
#         (sor2_elem0, ..., sor2_elem4),
#         (sor3_elem0, ..., sor3_elem6) )
#
# Az elemek értéke: 1..14 (lapocska) vagy None (üres hely).
# Elérés: s[sor][poz]
# Módosítás: mivel tuple, másoláskor listává alakítjuk, majd visszafagyasztjuk.
#
# KEZDŐÁLLAPOT
# ------------
#              4
#           9  11   7
#       10   8  14   6   5
#    2   _   _  13   1   3  12
#
#   s₀ = ( (4,),
#           (9, 11, 7),
#           (10, 8, 14, 6, 5),
#           (2, None, None, 13, 1, 3, 12) )
#
# CÉLÁLLAPOT
# ----------
#              1
#           2   3   4
#        5   6   7   8   9
#    10  11  12  13  14   _   _
#
#   s* = ( (1,),
#           (2, 3, 4),
#           (5, 6, 7, 8, 9),
#           (10, 11, 12, 13, 14, None, None) )
#
# OPERÁTOROK HALMAZA
# ------------------
# Minden üres cella (sor_u, poz_u)-hoz annyi operátor tartozik,
# ahány szomszédja van. Az operátor a szomszéd lapocskáját az üres helyre tolja.
# op(u, v): s → s', ahol s'[u] = s[v], s'[v] = None
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Pre(op(u, v), s) ≡
#     s[sor_u][poz_u] = None         (u cella üres)
#   ∧ (sor_v, poz_v) ∈ szomszédok(sor_u, poz_u)
#   ∧ s[sor_v][poz_v] ≠ None         (v cellában van lapocska)
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# γ(op(u, v), s):
#   Legyen s' az s tuple-mátrix másolata (listává alakítva)
#   s'[sor_u][poz_u] ← s[sor_v][poz_v]
#   s'[sor_v][poz_v] ← None
#   return tuple(tuple(sor) for sor in s')
#
# HEURISZTIKA (BFS-távolság összeg)
# ----------------------------------
# h(s) = Σ_{lapocska ∈ 1..14}  BFS_dist(jelenlegi_poz(lapocska), cél_poz(lapocska))
# Admissible: minden lépés csak egy lapocskát mozgat egyet.
# =============================================================================


SOROK = 4

KEZDŐ = (
                   (4,),
              (9,   11, 7),
         (10,  8,   14, 6, 5),
    (2, None, None, 13, 1, 3, 12)
    )

TESZT = (
                 (1,),
             (2,  3,  4),
         (5,  6,  None,  None,  9),
    (10, 11, 12, 13, 14, 15, 16)
    )

CÉL = (
                 (1,),
             (2,  3,  4),
         (5,  6,  7,  8,  9),
    (10, 11, 12, 13, 14, None, None)
    )

def felfelé_mutat(sor, poz):
    return poz % 2 == 0

def szomszédok(állapot, sor, poz):
    szomszédok = []
    
    if poz >= 2 and állapot[sor][poz-1] is None:    # bal-ról tol jobbra, közte None
        szomszédok.append((sor, poz - 2))
    if poz <= 2 * sor - 2 and állapot[sor][poz+1] is None:   # jobb-ról tol balra, közte None
        szomszédok.append((sor,poz + 2))

    if felfelé_mutat(sor, poz): # ha felfelé mutat (páratlan)
        if sor >= 1:
            if poz >= 2 and állapot[sor][poz-1] is None:  # balra mellette None
                szomszédok.append((sor-1,poz-2))    # bal fentről tol !! LE !!
            if poz <= 2 * sor - 2 and állapot[sor][poz+1] is None:   # jobbra mellette None
                szomszédok.append((sor-1,poz))      # jobb fentről tol !! LE !!
        if sor <= SOROK - 2:
            if állapot[sor+1][poz+1] is None:   # alatta None
                szomszédok.append((sor+1,poz))      # jobb lentről lentről tol !! FEL !!
                szomszédok.append((sor+1,poz+2))    # bal lentről  lentről tol !! FEL !!
    else:   # ha lefelé mutat (páros)
        if sor >= 2:
            if poz >= 2 and állapot[sor-1][poz-1] is None:  # fölötte none
                szomszédok.append((sor-1,poz-2))    # bal fentről tol !! LE !!
            if poz <= 2 * sor - 3 and állapot[sor-1][poz-1] is None:
                szomszédok.append((sor-1,poz))      # jobb fentről tol !! LE !!
        if sor <= SOROK - 2:
            if poz >= 1 and állapot[sor][poz-1] is None:    # balra mellette none
                szomszédok.append((sor+1,poz))      # bal lentről tol !! FEL !!
            if poz <= 2 * sor - 1 and állapot[sor][poz+1] is None:  #jobbra mellette none
                szomszédok.append((sor+1,poz+2))    # jobb lentről tol !! FEL !!

    return szomszédok


def állapot_másolat_módosítva(állapot, sor_u, poz_u, sor_v, poz_v):
    sorok = [list(sor) for sor in állapot]
    sorok[sor_u][poz_u], sorok[sor_v][poz_v] = sorok[sor_v][poz_v], sorok[sor_u][poz_u]
    return tuple(tuple(sor) for sor in sorok)

def üres_helyek(állapot):
    helyek = []
    for sor, sor_tartalom in enumerate(állapot):
        #print(f"enumerate(a): {sor = }   {sor_tartalom = }")
        for poz, érték in enumerate(sor_tartalom):
            #print(f"enumerate(sor_tartalom): {poz = }   {érték = }")
            if érték is None:
                helyek.append((sor, poz))
    return helyek


class Háromszög(Feladat):
    def __init__(self):
        self.kezdő = KEZDŐ
        self.cél   = CÉL

    def célteszt(self, a):
        return a == CÉL

    def rákövetkező(self, a):
        gyerekek = []
        for sor_ü, poz_ü in üres_helyek(a):
            for sor_l, poz_l in szomszédok(a, sor_ü, poz_ü):
                lapocska = a[sor_l][poz_l]
                if lapocska is not None:
                    lista_állapot = [list(sor) for sor in a]
                    lista_állapot[sor_ü][poz_ü], lista_állapot[sor_l][poz_l] = lista_állapot[sor_l][poz_l], lista_állapot[sor_ü][poz_ü]
                    új_állapot = tuple(tuple(sor) for sor in lista_állapot)
                    #új_állapot = állapot_másolat_módosítva(a, sor_ü, poz_ü, sor_l, poz_l)
                    gyerekek.append((f"{lapocska}: ({sor_l},{poz_l}) -> ({sor_ü},{poz_ü})", új_állapot))
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    nem_helyén = 0
    for sor in range(SOROK):
        for poz in range(2 * sor + 1):
            v = a[sor][poz]
            if v is not None and v != CÉL[sor][poz]:
                nem_helyén = nem_helyén + 1
    return nem_helyén


if __name__ == '__main__':
    feladat = Háromszög()

    kov = feladat.rákövetkező(TESZT)
    for n, t in enumerate(kov):
        print(f"{n+1}. gyerek:  {t}")
        for s in t[-1]:
            print(f"{s}")
        print()

    result1 = best_first(feladat, heurisztika)
    print(f"Best_first:\t {result1.megoldás()}")

    #result2 = szélességi_fakereső(feladat)
    #print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    #result3 = mélységi_gráfkereső(feladat)
    #print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

    #result4 = a_csillag(feladat, heurisztika)
    #print(f"a_csillag:\t {result4.megoldás()}")