from keres import *

class Hanoi(Feladat): # öröklődés

    def __init__(self, ke,c):
        self.kezdő = ke
        self.cél = c
        self.N = len(ke)

    def célteszt(self,a): # a=(a1,a2,...,an)
        return a == self.cél

    def rákövetkező(self,a ): # a=(a1,a2,...,an)
        gyerekek = []

        for melyiket in range(0,self.N):
            for hova in ['P','Q','R']:
                tmp = True # feltételezem, hogy  alkalmazható
                if a[melyiket] != hova:
                    for i in range(0,melyiket):
                        if a[i] !=  a[melyiket] and a[i] != hova:
                            pass
                        else:
                            tmp = False
                            break
                else:
                    tmp = False

                if tmp :
                    gyerek_allapot = list(a)
                    gyerek_allapot[melyiket] = hova
                    gyerekek.append((f"{melyiket}-> {hova}",tuple(gyerek_allapot)))

        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    n = len(a) # korongok száma
    # megszámoljuk hány legnagyobb korong nincs még a helyén:
    for i in range(len(a)-1, -1, -1):
        if a[i] == 'R':
            n = n-1
        else:
            break

    return 2**n -1


if __name__ == '__main__':
    feladat = Hanoi (('P','P','P','P'),('R','R','R','R'))
    feladat2 = Hanoi(('P', 'P', 'P'), ( 'R', 'R', 'R'))

    print("szélességi gráfkereső:")
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    ut = result1.út()
    ut.reverse()
    print(ut)

    print("mélységi gráfkereső:")
    result2 = mélységi_gráfkereső(feladat)
    print(result2.megoldás())
    ut = result2.út()
    ut.reverse()
    print(ut)

    print("best_first")
    result3 = best_first(feladat, heurisztika)
    print(result3.megoldás())

