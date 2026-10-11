from my_jatek import *

def make_tuple(s):
    szamok = [int(x.strip()) for x in s.split(",")]
    return tuple( (szamok[i], szamok[i+1]) for i in range(0, len(szamok), 2))

class KorongJatek(Jatek):
    SOROK = 6
    OSZLOPOK = 7
    SOTET = [(2,4), (3,2)]

    def __init__(self):
        piros = set()
        kek = set()

        for oszlop in range(self.OSZLOPOK):
                piros.add((0, oszlop))

        for oszlop in range(self.OSZLOPOK):
                kek.add((self.SOROK-1, oszlop))

        self.kezdo = Struct(
            kovetkezik='P',     # piros kezd
            piros=frozenset(piros),
            kek=frozenset(kek),
            eredmeny=0      # 0 = folyamatban, 1 = P nyert, -1 = K nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: ((honnan_sor, honnan_oszlop), (hova_sor, hova_oszlop))
        """
        lepesek = []
        piros, kek = allapot.piros, allapot.kek

        if allapot.kovetkezik == 'P': # Piros: lefelé
            sajat = piros
            ellenfel = kek
            irany = 1
        else:   # Kék: felfelé
            sajat = kek
            ellenfel = piros
            irany = -1

        foglalt = sajat | ellenfel

        for (sor, oszlop) in sajat:
            # Egyeness
            uj_sor = sor + irany
            hova = (uj_sor, oszlop)
            if (0 <= uj_sor < self.SOROK and
                    hova not in foglalt and hova not in self.SOTET):
                lepesek.append(((sor, oszlop), hova))

            # Átló
            for d_oszlop in [-1, 1]:
                uj_oszlop = oszlop + d_oszlop
                hova = (uj_sor, uj_oszlop)
                if (0 <= uj_sor < self.SOROK and 0 <= uj_oszlop < self.OSZLOPOK and
                        hova not in self.SOTET):
                    if hova in ellenfel:
                        lepesek.append(((sor, oszlop), hova))
                    elif hova not in foglalt:
                        lepesek.append(((sor, oszlop), hova))

        return lepesek

    def lep(self, lepes, allapot):
        """
        Lépés: ((honnan_sor, honnan_oszlop), (hova_sor, hova_oszlop))
        """
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in self.legalis_lepesek(allapot):
            return allapot   # téves lépés

        honnan, hova = lepes
        piros = set(allapot.piros)
        kek = set(allapot.kek)

        if allapot.kovetkezik == 'P':
            piros.remove(honnan)
            piros.add(hova)
            kek.discard(hova)   # ütés
        else:
            # Kék lép: hasonlóan
            kek.remove(honnan)
            kek.add(hova)
            piros.discard(hova) # ütés

        uj_piros = frozenset(piros)
        uj_kek = frozenset(kek)
        kovetkezo = if_(allapot.kovetkezik == 'K', 'P', 'K')
        return Struct(
            kovetkezik=kovetkezo,
            piros=uj_piros,
            kek=uj_kek,
            eredmeny=self.ertekel(Struct(
                    kovetkezik=kovetkezo,
                    piros=uj_piros,
                    kek=uj_kek,
                    eredmeny=0 )
                    )
            )

    def ertekel(self, kov_allapot):
        if not self.legalis_lepesek(kov_allapot):
            if kov_allapot.kovetkezik == 'P': return -1 
            else:                            return 1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'P', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """yert állás (az aktuális játékos nem tud lépni)"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        tabla = {}
        for mezo in allapot.piros:
            tabla[mezo] = 'P'
        for mezo in allapot.kek:
            tabla[mezo] = 'K'
        for mezo in self.SOTET:
            tabla[mezo] = 'X'

        print("  " + " ".join(str(oszl) for oszl in range(self.OSZLOPOK)))  # header
        for sor in range(self.SOROK):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.OSZLOPOK))
            )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = KorongJatek()

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: honnan_sor, honnan_oszl, hova_sor, hova_oszl | példa: 1,1,1,2\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
