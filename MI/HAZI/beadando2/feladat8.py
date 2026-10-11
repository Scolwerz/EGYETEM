from my_jatek import *

class Szamjegyes(Jatek):
    def __init__(self, szam):
        szamjegyek = tuple(int(c) for c in str(szam))

        self.kezdo = Struct(
            kovetkezik='A',     # A kezd
            jegyek=szamjegyek,
            eredmeny=0      # 0 = folyamatban, 1 = A nyert, -1 = B nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés:  ('D', index) = 'index' jegx csökkentéss
                ('T', hossz) = utolsó 'hossz' törlése
        """
        szamjegyek = allapot.jegyek
        n = len(szamjegyek)

        lepesek = []

        # csökkentes
        for i, jegy in enumerate(szamjegyek):
            if jegy > 0:
                lepesek.append(('D', i))

        # törlés
        for i in range(n):
            if szamjegyek[i] == 0:
                hossz = n - i
                lepesek.append(('T', hossz))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            mode, val = lepes.split(',')
            lepes = (mode.strip(), int(val.strip()))
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        tipus, ertek = lepes
        szamjegyek = list(allapot.jegyek)

        if tipus == 'D':
            szamjegyek[ertek] -= 1
        elif tipus == 'T':
            szamjegyek = szamjegyek[:-ertek]

        uj_jegyek = tuple(szamjegyek)

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'A', 'B', 'A'),
            jegyek=uj_jegyek,
            eredmeny=self.ertekel(uj_jegyek, allapot.kovetkezik)
        )

    def ertekel(self, jegyek, jatekos):
        if not jegyek:
            if jatekos == 'A': return 1
            else:              return -1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'A', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nincs több lehetséges lépés"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        print("Szám: " + ''.join(str(j) for j in allapot.jegyek) , end=' ')
        print(f"(idx: 0 - {len(allapot.jegyek)-1}) (hossz: {len(allapot.jegyek)})")

        print(f"Következik: {allapot.kovetkezik} | Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = Szamjegyes("5231205661024")

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: csökkent(D), index VAGY töröl(T), hossz | példa: D,1 VAGY T,5\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
