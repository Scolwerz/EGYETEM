from my_jatek import *

SZOMSZEDOK = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def negy_sajat_szomszed(lepes, tabla, jatekos, N):
    sor, oszlop = lepes

    for dsor, doszlop in SZOMSZEDOK:
        uj_sor, uj_oszlop = sor + dsor, oszlop + doszlop

        if not (0 <= uj_sor < N and 0 <= uj_oszlop < N):
            return False
        
        if tabla.get((uj_sor, uj_oszlop)) != jatekos:
            return False
        
    return True

class Szomszed(Jatek):
    N = 5

    def __init__(self):
        lepesek = [(sor, oszlop) for sor in range(self.N) for oszlop in range(self.N)]

        self.kezdo = Struct(
            kovetkezik='A',     # A játékos kezd
            tabla={},
            lepesek=lepesek,
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (sor, oszlop)
        """
        return allapot.lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        sor, oszlop = lepes
        jatekos = allapot.kovetkezik

        uj_tabla = allapot.tabla.copy()
        uj_tabla[lepes] = jatekos

        # Szabad mezők frissítése
        uj_lepesek = list(allapot.lepesek)
        uj_lepesek.remove(lepes)

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'A', 'B', 'A'),
            tabla=uj_tabla,
            lepesek=uj_lepesek,
            eredmeny=self.ertekel(lepes, uj_tabla, allapot.kovetkezik)
        )

    def ertekel(self, lepes, tabla, jatekos):
        """
        for sor in range(1, self.N-1):
            for oszlop in range(1, self.N-1):
                kord = (sor, oszlop)
                if negy_sajat_szomszed(kord, tabla, jatekos, self.N):
                    if jatekos == 'A': return -1
                    else:              return 1
        """
        if negy_sajat_szomszed(lepes, tabla, jatekos, self.N):
            if jatekos == 'A': return -1
            else:              return 1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás vagy a tele tábla"""
        return allapot.eredmeny != 0 or not allapot.lepesek

    def kiir(self, allapot):
        tabla = allapot.tabla
    
        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
            )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = Szomszed()
    
    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: sor, oszlop | példa: 1,1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
