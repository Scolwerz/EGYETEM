from keres import *
class KancsoFeladat (Feladat): # öröklődés
    def __init__(self, ke, c, max):
        self.kezdő = ke
        self.cél = c
        self.MAX = max

    def célteszt(self, a): # a = (a1,a2,a2) állapot
        return a[0] == self.cél or a[1] == self.cél or a[2] == self.cél

    def rákövetkező(self, a): # a = (a1,a2,a2) állapot
        gyerekek = []
        a1,a2,a3 = a
        max1, max2, max3 = self.MAX

        # tölt 1,2 alkalmazási előfeltétele:
        if a1 != 0 and a2 != max2:
            T = min(a1,max2-a2)
            gyerekek.append(("tölt 1->2",(a1-T, a2+T, a3)))

        # tölt 1,3 alkalmazási előfeltétele:
        if a1 != 0 and a3 != max3:
            T = min(a1, max3 - a3)
            gyerekek.append(("tölt 1->3", (a1 - T, a2 , a3+T)))

        # tölt 2,1 alkalmazási előfeltétele:
        if a2 != 0 and a1 != max1:
            T = min(a2, max1 - a1)
            gyerekek.append(("tölt 2->1", (a1 + T, a2-T , a3)))

        # tölt 2,3 alkalmazási előfeltétele:
        if a2 != 0 and a3 != max3:
            T = min(a2, max3 - a3)
            gyerekek.append(("tölt 2->3", (a1 , a2-T , a3+T)))

         # tölt 3,1 alkalmazási előfeltétele:
        if a3 != 0 and a1 != max1:
            T = min(a3, max1 - a1)
            gyerekek.append(("tölt 3->1", (a1 + T, a2 , a3-T)))

        # tölt 3,2 alkalmazási előfeltétele:
        if a3 != 0 and a2 != max2:
            T = min(a3, max2 - a2)
            gyerekek.append(("tölt 3->2", (a1 , a2 + T, a3 - T)))

        return gyerekek



def heurisztika(csúcs):
    a = csúcs.állapot
    return min([abs(a[0]-4), abs(a[1]-4), abs(a[2]-4)])

if __name__ == '__main__':
    feladat = KancsoFeladat((0,0,8),4,(3,5,8))

    print("szélességi fakereső:")
    result1 = szélességi_fakereső(feladat)
    print(result1.megoldás())
    ut = result1.út()
    ut.reverse()
    print(ut)

    print("mélységi fakereső:")
    result2 = mélységi_fakereső(feladat)
    print(result2.megoldás())
    ut = result2.út()
    ut.reverse()
    print(ut)

    print("best_first")
    result3 = best_first(feladat, heurisztika)
    print(result3.megoldás())











