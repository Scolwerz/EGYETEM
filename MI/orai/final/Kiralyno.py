from keres import *

class Kiralyno(Feladat):
    def __init__(self,ke,c):
        self.kezdő = ke
        self.cél = c
        self.N = len(ke) - 1

    def célteszt(self,a):  # a = (a1,a2,...,an,s)
        return a[self.N] == self.cél # s==N+1?

    def rákövetkező(self,a):   # a = (a1,a2,...,an,s)
        gyerekek = []
        s = a[self.N]
        for i in range(1,self.N+1):
            előfeltétel = True # lerak (s,i) ???
            for m in range(1,s): #  minden m<s:
                if a[m-1] != i and abs(s-m) != abs(i-a[m-1  ]):
                    pass
                else:
                    előfeltétel = False
                    break

            if előfeltétel:
                uj_allapot =list(a)
                uj_allapot[s-1] = i  # (s,i) lerakás
                uj_allapot[self.N] = s+1
                gyerekek.append((f"({s},{i})",tuple(uj_allapot)))

        return  gyerekek



if __name__ == '__main__':
    feladat1 = Kiralyno((0,0,0,0,1),5)
    feladat2 = Kiralyno((0,0,0,0,0,0,0,0,1),9)
    print("szélességi fakereső:")
    result1 = szélességi_fakereső(feladat2)
    print(result1.megoldás())
    ut = result1.út()
    ut.reverse()
    print(ut)

    print("mélységi fakereső:")
    result2 = mélységi_fakereső(feladat2)
    print(result2.megoldás())
    ut = result2.út()
    ut.reverse()
    print(ut)


