
from my_jatek import *

class KavicsKupac(Jatek):
    def __init__(self, kupac1=9, kupac2=8):
        
        self.kezdo = Struct(
            kovetkezik='A',     # 'A' kezd
            kupac1=kupac1,
            kupac2=kupac2,
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (melyik, mennyit)
        (1, k) = k kavicsot vesz az 1 kupacból
        (3, k) = k kavicsot vesz el mind a kettő kupacból
        """
        lepesek = []
        k1, k2 = allapot.kupac1, allapot.kupac2

        for k in range(1, k1 + 1):
            lepesek.append((1, k))

        for k in range(1, k2 + 1):
            lepesek.append((2, k))

        for k in range(1, min(k1, k2) + 1):
            lepesek.append((3, k))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        melyik, mennyi = lepes
        k1, k2 = allapot.kupac1, allapot.kupac2

        if melyik == 1:
            k1 -= mennyi
        elif melyik == 2:
            k2 -= mennyi
        elif melyik == 3:
            k1 -= mennyi
            k2 -= mennyi

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'A', 'B','A'),
            kupac1=k1,
            kupac2=k2,
            eredmeny=self.ertekel(k1, k2, allapot.kovetkezik)
        )

    def ertekel(self, kupac1, kupac2, jatekos):
        if kupac1 == 0 and kupac2 == 0:
            if jatekos == 'A': return 1
            else: return -1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás (mindkét kupac üres)"""
        return allapot.eredmeny != 0

    def kiir(self, allapot):
        print(f"Kupac 1: {allapot.kupac1}")
        print(f"Kupac 2: {allapot.kupac2}")

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = KavicsKupac(kupac1=11, kupac2=13)
    
    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: kupac, mennyit | példa: 1,1  | 3 = mindkét\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
