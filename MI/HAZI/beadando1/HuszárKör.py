from keres import *

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
            if (sor + sorlépés, oszlop + oszloplépés) == a[0]:
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
    if not lépések: # nincs lehetséges lépés
        if len(a) < len(ÉRVÉNYES_MEZŐK):
            return 999
        return 0

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
    