from my_jatek import *

HUSZAR_LEPESEK = [(1,2), (1,-2), (-1,2), (-1,-2), (2,-1), (2,1),(-2,-1), (-2,1)]

class HuszarJatek(Jatek):
    N = 8

    def __init__(self, sotet=(0, 1), vilagos=(7, 6)):
        

        self.kezdo = Struct(
            kovetkezik='S',     # sötét kezd
            sotet=sotet,
            vilagos=vilagos,
            latott=((sotet, vilagos),),
            eredmeny=0      # 0 = folyamatban, 1 = S nyert, -1 = V nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (uj_sor, uj_oszlop)
        """
        if allapot.kovetkezik == 'S': poz = allapot.sotet
        else:                         poz = allapot.vilagos

        n = self.N
        sor, oszlop = poz

        lepesek = []
        for sorlépés, oszloplépés in HUSZAR_LEPESEK:
            uj_poz = (sor + sorlépés, oszlop + oszloplépés)
            if uj_poz not in allapot.latott and 0 <= uj_poz[0] < n and 0 <= uj_poz[1] < n:
                lepesek.append(uj_poz)

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés
        
        if allapot.kovetkezik == 'S':
            uj_sotet = lepes
            uj_vilagos = allapot.vilagos
        else:   # 'V'
            uj_sotet = allapot.sotet
            uj_vilagos = lepes

        uj_latott = allapot.latott + (lepes,)
        kovetkezo = if_(allapot.kovetkezik == 'V', 'S', 'V')
        return Struct(
            kovetkezik=kovetkezo,
            sotet=uj_sotet,
            vilagos=uj_vilagos,
            latott=uj_latott,
            eredmeny=self.ertekel(Struct(
                    kovetkezik=kovetkezo,
                    sotet=uj_sotet,
                    vilagos=uj_vilagos,
                    latott=uj_latott,
                    eredmeny=0 )
                    )
            )

    def ertekel(self, kov_allapot):
        if kov_allapot.kovetkezik == 'S': kov_poz = kov_allapot.sotet
        else:              kov_poz = kov_allapot.vilagos

        if not self.legalis_lepesek(kov_allapot):
            if kov_allapot.kovetkezik == 'S': return -1
            else:              return 1    # V
            
        return 0

    def hasznossag(self, allapot, jatekos):
         return if_(jatekos == 'S', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás (az aktuális játékos nem tud lépni)"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        tabla = {}

        for mezo in allapot.latott:
            tabla[mezo] = '*'
        tabla[allapot.sotet] = 'S'
        tabla[allapot.vilagos] = 'V'

        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
            )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = HuszarJatek(sotet=(0, 1), vilagos=(5, 7))

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: sor, oszlop | példa: 1,1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
