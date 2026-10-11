from my_jatek import *

def make_frset(s):
    szamok = [int(x.strip()) for x in s.split(",")]
    return frozenset( (szamok[i], szamok[i+1]) for i in range(0, len(szamok), 2))

class KavicsTabla(Jatek):
    N = MAX_LEVESZ = 4

    def __init__(self):
        lepesek = frozenset( (sor, oszlop) for sor in range(self.N) for oszlop in range(self.N))
        
        self.kezdo = Struct(
            kovetkezik='A',     # A  kezd
            kavicsok=lepesek,
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: set( (sor, oszlop), )
        """
        szakaszok = []

        # sor
        for sor in range(self.N):
            oszlopok = sorted( oszlop for (s, oszlop) in allapot.kavicsok if s == sor )
            for kezd in range(len(oszlopok)):
                for veg in range(kezd + 1, min(kezd + self.MAX_LEVESZ + 1, len(oszlopok) + 1)):
                    reszsor = oszlopok[kezd:veg]
                    if reszsor[-1] - reszsor[0] == len(reszsor) - 1:
                        szakasz = frozenset((sor, o) for o in reszsor)
                        szakaszok.append(szakasz)

        # oszlop
        for oszlop in range(self.N):
            sorok = sorted(sor for (sor, o) in allapot.kavicsok if o == oszlop)
            for kezd in range(len(sorok)):
                for veg in range(kezd + 1 + 1, min(kezd + self.MAX_LEVESZ + 1, len(sorok) + 1)):
                    reszsor = sorok[kezd:veg]
                    if reszsor[-1] - reszsor[0] == len(reszsor) - 1:
                        szakasz = frozenset((s, oszlop) for s in reszsor)
                        szakaszok.append(szakasz)

        return szakaszok

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_frset(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        uj_kavicsok = allapot.kavicsok - lepes

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'A', 'B', 'A'),
            kavicsok=uj_kavicsok,
            eredmeny=self.ertekel(uj_kavicsok, allapot.kovetkezik)
        )

    def ertekel(self, kavicsok, jatekos):
        if not kavicsok:
            if jatekos == 'A': return 1
            else:              return -1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás (üres a tábla)."""
        return allapot.eredmeny != 0 or not allapot.kavicsok

    def kiir(self, allapot):
        tabla = {}
        for mezo in allapot.kavicsok:
            tabla[mezo] = 'X'

        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
            )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = KavicsTabla()

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: levesz_1_sor, levesz_1_oszl, levesz_2_sor, levesz_2_oszl, ... | példa: 1,1,1,2,1,3\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
