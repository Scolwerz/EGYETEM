from keres import *
class Kiralyno(Feladat): # öröklődés
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c
        self.N = len(ke)-1

    def célteszt(self, a): # a= (a1,a2,....,an,s)
        return a[self.N] == self.cél

    def rákövetkező(self,a):# a= (a1,a2,....,an,s)
        gyerekek = []
        s = a[self.N] # a következő sor indexe
        for i in range(1,self.N+1):
            előfeltétel = True # lerak (s,i) alkalmazható ????
            for m  in range(1,s): # minden m<s:
                if a[m-1] != i and abs(m-s) != abs(a[m-1]-i):
                    előfeltétel = True
                else:
                    előfeltétel = False
                    break

            if előfeltétel :
                uj_allapot = list(a)
                uj_allapot[s-1] = i
                uj_allapot[self.N] = s+1
                gyerekek.append(("oprator",tuple(uj_allapot)))

        return  gyerekek



if __name__ == '__main__':
    feladat = Kiralyno((0,0,0,0,0,0,0,0,1),9)
    feladat2 = Kiralyno((0,0,0,0,1),5)
    print("szélességi kereső")
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    utam = result1.út()
    utam.reverse()
    print(utam)



