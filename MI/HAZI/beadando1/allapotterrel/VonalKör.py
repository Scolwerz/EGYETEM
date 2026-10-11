from keres import *

# =============================================================================
# MATEMATIKAI-LOGIKAI ÉS HALMAZELMÉLETI LEÍRÁS – SLITHERLINK
# =============================================================================
#
# A tábla: szabályos 8×8-as rácstábla.
#   M = {(i,j) | 0≤i,j≤7}
#   |M| = 64 mező
#
# MEGJELÖLT MEZŐK (PONTOK)
# ------------------------
# P ⊂ M, azon mezők halmaza, ahol a vonalon 90 fokos törés kötelező:
#   P = {(0,0),(0,4),(1,3),(1,6),(2,2),(3,5),(4,1),(4,4),
#         (5,2),(5,7),(6,0),(6,5),(7,3),(7,7)}
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot: a meglátogatott mezők sorrendje tuple-ként:
#   S = ( (sor₁,oszlop₁), (sor₂,oszlop₂), ..., (sorₖ,oszlopₖ) )
# Az aktuális pozíció mindig az utolsó elem: s[-1]
# Az aktuális haladási irány az utolsó két elem különbsége:
#   irány(s) = s[-1] - s[-2]   (ha |s| ≥ 2)
# A tuple hasítható → berakható a gráfkereső kifejtési_sor set-jébe.
#
# KEZDŐÁLLAPOT
# ------------
# s₀ = ( (0,0), )
# A vonal a (0,0) mezőn kezdődik (amely egyben PONT is),
# az induló irány még nincs meghatározva.
#
# CÉLÁLLAPOT
# ----------
# s* olyan tuple, amelyre:
#   len(s*) = ÖSSZES_MEZŐ = 64   (minden mező pontosan egyszer szerepel)
#   ÉS a záródáshoz szomszédos a kezdőmezővel:
#       s*[-1] és s*[0] = (0,0) között távolság = 1 (vízszintesen vagy függőlegesen)
#   ÉS a záró él iránya konzisztens a (0,0)-beli kanyarfeltétellel
#       (ha (0,0) ∈ P, akkor a belépő és kilépő irány merőleges)
#
# OPERÁTOROK HALMAZA
# ------------------
# Az aktuális mezőről 4 szomszédos irányba léphetünk:
#   D = {(-1,0),(1,0),(0,-1),(0,1)}
# Operátor op(d) ahol d ∈ D:
#   op(d) : s → s + (s[-1]+d,)    (tuple végéhez fűzzük az új mezőt)
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Pre(op(d), s) ≡
#     s[-1]+d ∈ M              (a célmező a táblán belül van)
#   ∧ s[-1]+d ∉ s               (még nem látogattuk meg, kivéve ha ez a záró lépés)
#   ∧ kanyarfeltétel(s, d):
#       – ha |s| ≥ 2 és s[-1] ∈ P:
#           az új irány d merőleges az eddigi irányra
#           (skalárszorzat(korábbi_irány, d) = 0)
#       – ha |s| ≥ 2 és s[-1] ∉ P:
#           az új irány d azonos az eddigi irányra
#           (skalárszorzat(korábbi_irány, d) ≠ 0, azaz nem kanyarodik)
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# γ(op(d), s) = s + ( (s[-1][0]+d[0], s[-1][1]+d[1]), )
#
# =============================================================================


"""RÁCSMÉRET = 8
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
}"""


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
            # Vissza a startba csak akkor, ha már minden mezőt bejűrtunk
            """if szomszéd == a[0]:
                if len(a) == ÖSSZES_MEZŐ and irány_helyes(a, szomszéd):
                    új_állapot = a + (szomszéd,)
                    gyerekek.append((f"{aktuális}->{szomszéd}", új_állapot))
            
            elif szomszéd not in a:
                if irány_helyes(a, szomszéd):
                    új_állapot = a + (szomszéd,)
                    gyerekek.append((f"{aktuális}->{szomszéd}", új_állapot))"""

            if szomszéd in a:
                continue
            if not irány_helyes(a, szomszéd):
                continue
            új_állapot = a + (szomszéd,)
            gyerekek.append((f"{aktuális}->{szomszéd}", új_állapot))

        return gyerekek


def heurisztika(csúcs):
    meglátogatott = len(csúcs.állapot)
    összes = RÁCSMÉRET * RÁCSMÉRET
    return összes - meglátogatott


if __name__ == '__main__':
    feladat = VonalKör()

    kov = feladat.rákövetkező(((0,2),))


    """
    aaa = (
        (0,0),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
        (2,7),(2,6),(2,5),(2,4),(2,3),(2,2),(2,1),(2,0),
        (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),
        (4,7),(4,6),(4,5),(4,4),(4,3),(4,2),(4,1),(4,0),
        (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),
        (6,7),(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),
        (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),
        (0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(0,1)
        )
    kov = feladat.rákövetkező(aaa)
    """

    for n, t in enumerate(kov):
        print(f"{n+1}. gyerek:  {t}")
        print()

    #result1 = best_first(feladat, heurisztika)
    #print(f"Best_first:\t\t {result1.megoldás()}")

    result2 = szélességi_fakereső(feladat)
    print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")

