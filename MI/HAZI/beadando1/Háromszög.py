from keres import *

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


def érvényes_szomszédok(állapot, sor, poz):
    szomszédok = []
    
    if poz >= 2 and állapot[sor][poz-1] is None:    # bal-ról tol jobbra, közte None
        szomszédok.append((sor, poz - 2))
    if poz <= 2 * sor - 2 and állapot[sor][poz+1] is None:   # jobb-ról tol balra, közte None
        szomszédok.append((sor,poz + 2))

    if poz % 2 == 0: # ha felfelé mutatő kis háromszög (páratlan)
        if sor >= 1:
            if poz >= 2 and állapot[sor][poz-1] is None:  # balra mellette None
                szomszédok.append((sor-1,poz-2))    # bal fentről tol !! LE !!
            if poz <= 2 * sor - 2 and állapot[sor][poz+1] is None:   # jobbra mellette None
                szomszédok.append((sor-1,poz))      # jobb fentről tol !! LE !!

        if sor <= len(állapot) - 2:
            if állapot[sor+1][poz+1] is None:   # alatta None
                szomszédok.append((sor+1,poz))      # jobb lentről lentről tol !! FEL !!
                szomszédok.append((sor+1,poz+2))    # bal lentről  lentről tol !! FEL !!
    
    else:   # ha lefelé mutat (páros)
        if sor >= 2:
            if poz >= 2 and állapot[sor-1][poz-1] is None:  # fölötte none
                szomszédok.append((sor-1,poz-2))    # bal fentről tol !! LE !!
            if poz <= 2 * sor - 3 and állapot[sor-1][poz-1] is None:
                szomszédok.append((sor-1,poz))      # jobb fentről tol !! LE !!

        if sor <= len(állapot) - 2:
            if poz >= 1 and állapot[sor][poz-1] is None:    # balra mellette none
                szomszédok.append((sor+1,poz))      # bal lentről tol !! FEL !!
            if poz <= 2 * sor - 1 and állapot[sor][poz+1] is None:  #jobbra mellette none
                szomszédok.append((sor+1,poz+2))    # jobb lentről tol !! FEL !!

    return szomszédok


def üres_helyek(állapot):
    üresek = []
    for sor, sor_tartalom in enumerate(állapot):
        #print(f"enumerate(a): {sor = }   {sor_tartalom = }")
        for poz, érték in enumerate(sor_tartalom):
            #print(f"enumerate(sor_tartalom): {poz = }   {érték = }")
            if érték is None:
                üresek.append((sor, poz))
    return üresek


class Háromszög(Feladat):
    def __init__(self):
        self.kezdő = KEZDŐ
        self.cél   = CÉL

    def célteszt(self, a):
        return a == CÉL

    def rákövetkező(self, a):
        gyerekek = []
        for sor_ü, poz_ü in üres_helyek(a):
            for sor_l, poz_l in érvényes_szomszédok(a, sor_ü, poz_ü):
                lapocska = a[sor_l][poz_l]
                if lapocska is not None:
                    lista_állapot = [list(sor) for sor in a]
                    lista_állapot[sor_ü][poz_ü], lista_állapot[sor_l][poz_l] = lista_állapot[sor_l][poz_l], lista_állapot[sor_ü][poz_ü]
                    új_állapot = tuple(tuple(sor) for sor in lista_állapot)
                    gyerekek.append((f"{lapocska}: ({sor_l},{poz_l}) -> ({sor_ü},{poz_ü})", új_állapot))
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    nincs_helyén = 0
    for sor in range(len(csúcs.állapot)):
        for poz in range(2 * sor + 1):
            lapocska = a[sor][poz]
            if lapocska is not None and lapocska != CÉL[sor][poz]:
                nincs_helyén = nincs_helyén + 1
    return nincs_helyén


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