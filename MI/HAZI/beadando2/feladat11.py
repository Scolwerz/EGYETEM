from my_jatek import *

class OszthatoKupacok(Jatek):
    def __init__(self, kupacok):
        self.kezdo = Struct(
            kovetkezik='A',     # A  kezd
            kupacok=tuple(kupacok),
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (kupac, elvesz)
        """
        lepesek = []
        for i, meret in enumerate(allapot.kupacok):
            if meret > 1:
                for elvesz in [k for k in range(1, meret) if meret % k == 0]:
                    lepesek.append((i, elvesz))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        kupac, elvesz = lepes
        kupacok = list(allapot.kupacok)
        kupacok[kupac] -= elvesz
        uj_kupacok = tuple(kupacok)

        kovetkezo = if_(allapot.kovetkezik == 'A', 'B','A')
        return Struct(
            kovetkezik=kovetkezo,
            kupacok=uj_kupacok,
            eredmeny=self.ertekel(Struct(
                    kovetkezik=kovetkezo,
                    kupacok=uj_kupacok,
                    eredmeny=0 )
                    )
            )

    def ertekel(self, kov_allapot):
        if not self.legalis_lepesek(kov_allapot):
            if kov_allapot.kovetkezik == 'A': return -1
            else:                         return 1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nincs lehetséges lépés"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        for i, meret in enumerate(allapot.kupacok):
            print(f"  Kupac {i}: ({meret})")

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = OszthatoKupacok([6, 10, 15])
    
    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: kupac, mennyit | példa: 1,1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
