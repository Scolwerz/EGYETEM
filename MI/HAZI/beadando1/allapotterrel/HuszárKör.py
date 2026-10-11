from keres import *


# =============================================================================
# RÉGI
# =============================================================================
#
# A tábla: szabályos 8×8-as sakktábla, amelyből eltávolítjuk a négy
# sarokmezőt → M = {(i,j) | 0≤i,j≤7} \ {(0,0),(0,7),(7,0),(7,7)}
# |M| = 64 - 4 = 60 mező
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot: (aktuális_pozíció, már_meglátogatott_mezők_fagyasztott_halmaza)
#   S ⊆ M × P(M)
#   ahol P(M) a hatványhalmaz (frozenset a hasíthatóság miatt)
#
# KEZDŐÁLLAPOT
# ------------
# s₀ = ( (0,1), frozenset({(0,1)}) )
# A huszár az első sor bal szélső (nem-sarok) mezőjén áll,
# és csak ezt az egy mezőt látogatta meg.
#
# CÉLÁLLAPOT
# ----------
# s* = (p, frozenset(M))   ahol p ∈ M és a huszár egy lépéssel
# vissza tud jutni (0,1)-be.
# Feltétel: |meglátogatott| = 60  ÉS  (0,1) ∈ huszár_lépések(p)
#
# OPERÁTOROK HALMAZA
# ------------------
# A huszár 8 lehetséges ugrásiránya:
#   D = {(±1,±2), (±2,±1)}
# Operátor op(d) ahol d ∈ D:
#   op(d) : (p, V) → (p+d, V ∪ {p+d})
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Pre(op(d), (p,V)) ≡
#     p+d ∈ M           (a célmező a táblán van és nem sarok)
#   ∧ p+d ∉ V           (még nem látogattuk meg)
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# γ(op(d), (p,V)) = (p+d, V ∪ {p+d})
#
# HEURISZTIKA (Warnsdorff-szabály)
# ---------------------------------
# h(s) = az aktuális pozícióból elérhető, még nem látogatott mezők
#         mindegyikéről elérhető, még nem látogatott szomszédok
#         száma közül a minimum.
# Kis értéket preferál → a "zsákutcák" felé halad először.
# =============================================================================

# =============================================================================
# MATEMATIKAI-LOGIKAI ÉS HALMAZELMÉLETI LEÍRÁS – HUSZÁRJÁRAT
# =============================================================================
#
# A tábla: 4×4-es sakktábla, amelyből eltávolítjuk a négy sarokmezőt.
#   M = {(i,j) | 0≤i,j≤3} \ {(0,0),(0,3),(3,0),(3,3)}
#   |M| = 16 - 4 = 12 mező
#
# ÁLLAPOTTÉR
# ----------
# Egy állapot: a meglátogatott mezők sorrendje tuple-ként:
#   S = ( (sor₁,oszlop₁), (sor₂,oszlop₂), ..., (sorₖ,oszlopₖ) )
# Az aktuális pozíció mindig az utolsó elem: s[-1]
# A tuple hasítható → berakható a gráfkereső kifejtési_sor set-jébe.
#
# KEZDŐÁLLAPOT
# ------------
# s₀ = ( (0,1), )   – a huszár a (0,1) mezőn áll, csak azt látogatta meg
#
# CÉLÁLLAPOT
# ----------
# s* olyan tuple, amelyre:
#   len(s*) = ÖSSZES_MEZŐ_DB   (minden mező szerepel)
#   ÉS a huszár vissza tud lépni (0,1)-be:
#   ∃ (sorlépés,oszloplépés) ∈ D : s*[-1] + (sorlépés,oszloplépés) = (0,1)
#
# OPERÁTOROK HALMAZA
# ------------------
#   D = {(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)}
# Operátor op(d) ahol d ∈ D:
#   op(d) : s → s + (s[-1]+d,)    (tuple végéhez fűzzük az új mezőt)
#
# ALKALMAZÁSI ELŐFELTÉTEL
# -----------------------
# Pre(op(d), s) ≡
#     s[-1]+d ∈ M          (érvényes mező, nem sarok, nem kívül esik)
#   ∧ s[-1]+d ∉ s           (még nem látogattuk meg)
#
# ALKALMAZÁSI FÜGGVÉNY
# --------------------
# γ(op(d), s) = s + ( (s[-1][0]+sorlépés, s[-1][1]+oszloplépés), )
#
# HEURISZTIKA (Warnsdorff-szabály)
# ---------------------------------
# h(s) = az aktuális pozícióból elérhető, még nem látogatott szomszédok
#         mindegyikéről elérhető továbblépések számának minimuma.
# =============================================================================


HUSZÁR_LÉPÉSEK = [(1,2), (1,-2), (-1,2), (-1,-2), (2,-1), (2,1),(-2,-1), (-2,1)]

SARKOK = [(0,0), (0,3), (3,0), (3,3)]
ÉRVÉNYES_MEZŐK = [(i,j) for i in range(4) for j in range(4) if (i,j) not in SARKOK]

def lehetséges_lépések(poz, meglátogatott):
    sor, oszlop = poz
    lépések = []
    for sorlépés, oszloplépés in HUSZÁR_LÉPÉSEK:
        új_poz = (sor + sorlépés, oszlop + oszloplépés)
        if új_poz not in meglátogatott and új_poz in ÉRVÉNYES_MEZŐK:
            lépések.append(új_poz)
    return lépések

class HuszárKör(Feladat):
    def __init__(self):
        self.kezdő = ((0, 1), )
        self.cél = None

    def célteszt(self, a):
        #if len(a) == len(ÉRVÉNYES_MEZŐK) and a[-1] == self.kezdő[-1]:
 
        if len(a) != len(ÉRVÉNYES_MEZŐK):
            return False
        sor, oszlop= a[-1]
        for sorlépés, oszloplépés in HUSZÁR_LÉPÉSEK:
            if (sor + sorlépés, oszlop + oszloplépés) == self.kezdő[0]:
                return True
        return False

    def rákövetkező(self, a):
        gyerekek = [] 
        for lépés in lehetséges_lépések(a[-1], a):
            új_állapot = a + (lépés,)
            #print(f"{új_állapot = }")
            gyerekek.append((f"{lépés}", új_állapot))
        
        #print(gyerekek = )
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    pozíció = a[-1]
    lépések = lehetséges_lépések(pozíció,a)
    
    if not lépések:
        # Zsákutca, de még nem végeztünk → büntessük
        if len(a) < len(ÉRVÉNYES_MEZŐK):
            return 1000
        return 0
    # Minimális továbblépési lehetőség a szomszédokból
    return min(   len(  lehetséges_lépések(új_poz, a + (új_poz,))  )   for új_poz in lépések)


if __name__ == '__main__':
    feladat = HuszárKör()

    kov = feladat.rákövetkező(((0, 1), (2, 2)))

    for n, t in enumerate(kov):
        print(f"{n+1}. gyerek:  {t}")
        print()

    result1 = best_first(feladat, heurisztika)
    print(f"Best_first:\t\t {result1.megoldás()}")

    result2 = szélességi_fakereső(feladat)
    print(f"Szélességi_fakereső:\t {result2.megoldás()}")

    result3 = mélységi_gráfkereső(feladat)
    print(f"Mélységi_gráfkereső:\t {result3.megoldás()}")
    