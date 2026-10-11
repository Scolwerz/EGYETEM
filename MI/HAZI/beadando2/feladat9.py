
from my_jatek import *

class RekeszKavics(Jatek):
    REKESZEK = 32

    def __init__(self):
        self.kezdo = Struct(
            kovetkezik='A',     # A  kezd
            kavicsok=frozenset(),
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: index
        """
        kavicsok = allapot.kavicsok

        lepesek = []
        for i in range(self.REKESZEK):
            if i not in kavicsok and i-1 not in kavicsok and i+1 not in kavicsok:
                lepesek.append(i)
        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = int(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        uj_kavicsok = allapot.kavicsok | {lepes}

        kovetkezo = if_(allapot.kovetkezik == 'A', 'B', 'A')
        return Struct(
            kovetkezik=kovetkezo,
            kavicsok=uj_kavicsok,
            eredmeny=self.ertekel(Struct(
                    kovetkezik=kovetkezo,
                    kavicsok=uj_kavicsok,
                    eredmeny=0 )
                    )
            )
    
    def ertekel(self, kov_allapot):
        if not self.legalis_lepesek(kov_allapot):
            if kov_allapot.kovetkezik == 'A': return -1 
            else:                            return 1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nincs lehetséges lépés."""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        kavicsok = allapot.kavicsok

        print(''.join('O' if i in kavicsok else '_' for i in range(self.REKESZEK)))
        
        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = RekeszKavics()
    
    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: index | példa: 1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
