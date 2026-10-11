from keres import *

class KorongForgatás(Feladat):
    def __init__(self, kezdő):
        self.kezdő = kezdő
        self.N = len(kezdő)
        self.cél = tuple(range(1, self.N + 1))

    def célteszt(self, a):
        return a == self.cél

    def rákövetkező(self, a):
        gyerekek = []
        lista_állapot = list(a)
        for k in range(1, self.N + 1):
            új_állapot = lista_állapot[:k][::-1] + lista_állapot[k:]
            gyerekek.append((f"forgat({k})", tuple(új_állapot)))
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    n = len(a)
    már_rendezett = 0
    for i in range(n - 1, -1, -1):
        if a[i] == i + 1:
            már_rendezett += 1
        else:
            break
    return n - már_rendezett


if __name__ == '__main__':
    kezdő = (6, 7, 3, 2, 8, 5, 4, 1)

    feladat1 = KorongForgatás(kezdő)
 
    result1 = best_first(feladat1, heurisztika)
    print(f"best_first: \t\t{result1.megoldás()}")

    result2 = szélességi_gráfkereső(feladat1)
    print(f"Szélességi_gráfkereső: \t{result2.megoldás()}")
