from my_jatek import *

class KiralynoJatek(Jatek):
    N = 8
    CEL = (N-1, 0)  # bal alsó sarok

    def __init__(self, kezdo_pozicio=None):
        if kezdo_pozicio is None:
            kezdo_pozicio = (0, self.N - 1)

        self.kezdo = Struct(
            kovetkezik='A',     # A játékos kezd
            kiralyno=kezdo_pozicio, 
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (uj_sor, uj_oszlop)
        """
        sor, oszlop = allapot.kiralyno
        lepesek = []

        # balra
        for uj_oszlop in range(0, oszlop):
            lepesek.append((sor, uj_oszlop))

        # le
        for uj_sor in range(sor + 1, self.N):
            lepesek.append((uj_sor, oszlop))

        # bal-le átló
        for delta in range(1, min(self.N - sor, oszlop + 1)):
            uj_sor = sor + delta
            uj_oszlop = oszlop - delta
            if 0 <= uj_sor < self.N and 0 <= uj_oszlop < self.N:
                lepesek.append((uj_sor, uj_oszlop))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        uj_pozicio = lepes

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'A', 'B', 'A'),
            kiralyno=uj_pozicio,
            eredmeny=self.ertekel(uj_pozicio, allapot.kovetkezik)
        )

    def ertekel(self, poz, jatekos):
        if poz == self.CEL:
            if jatekos == 'A': return 1
            else:              return -1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás (elértük a célt: bal alsó sarok)"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        tabla = {}
        tabla[self.CEL] = '*'
        tabla[allapot.kiralyno] = 'Q'

        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
            )
        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = KiralynoJatek((0,6))

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: sor, oszlop | példa: 1,1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
