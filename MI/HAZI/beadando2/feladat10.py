from my_jatek import *

def make_tuple(s):
    szamok = [int(x.strip()) for x in s.split(",")]
    return tuple( (szamok[i], szamok[i+1]) for i in range(0, len(szamok), 2))


SZOMSZEDOK = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PirosKekKorong(Jatek):
    N = 5

    def __init__(self):
        kek_kezdo = frozenset([(0, self.N-1), (self.N-1, 0), (self.N//2, self.N//2)])
        piros_kezdo = frozenset((s, o) for s in range(self.N) for o in range(self.N) if (s, o) not in kek_kezdo )

        self.kezdo = Struct(
            kovetkezik='K',     # kék kezd
            kek=kek_kezdo,
            piros=piros_kezdo,
            eredmeny=0      # 0 = folyamatban, 1 = K nyert, -1 = P nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: ((honnan_sor, honnan_oszlop), (hova_sor, hova_oszlop))
        """
        lepesek = []
        piros, kek = allapot.piros, allapot.kek

        foglalt = piros | kek
        
        if allapot.kovetkezik == 'K':
            for (sor, oszlop) in kek:
                for dsor, doszlop in SZOMSZEDOK:
                    uj_sor, uj_oszlop = sor + dsor, oszlop + doszlop
                    hova = (uj_sor, uj_oszlop)
                    if (0 <= uj_sor < self.N and 0 <= uj_oszlop < self.N and
                            hova in piros):
                        lepesek.append(((sor, oszlop), hova))
        else:
            for (sor, oszlop) in piros:
                for dsor, doszlop in SZOMSZEDOK:
                    uj_sor, uj_oszlop = sor + dsor, oszlop + doszlop
                    hova = (uj_sor, uj_oszlop)
                    if (0 <= uj_sor < self.N and 0 <= uj_oszlop < self.N and
                            hova not in foglalt): 
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

        if allapot.kovetkezik == 'K':
            kek.remove(honnan)
            kek.add(hova)
            piros.discard(hova) # ütés
        else:
            piros.remove(honnan)
            piros.add(hova)

        uj_piros = frozenset(piros)
        uj_kek = frozenset(kek)
        kovetkezo = if_(allapot.kovetkezik == 'K', 'P', 'K')
        return Struct(
            kovetkezik=kovetkezo,
            kek=uj_kek,
            piros=uj_piros,
            eredmeny=self.ertekel(Struct(
                    kovetkezik=kovetkezo,
                    kek=uj_kek,
                    piros=uj_piros,
                    eredmeny=0 )
                    )
            )

    def ertekel(self, kov_allapot):
        keksorok = set(sor for (sor, _) in kov_allapot.kek)
        kekoszlopok = set(oszlop for (_, oszlop) in kov_allapot.kek)
        if len(keksorok) == 1: return -1
        if len(kekoszlopok) == 1: return -1

        if kov_allapot.kovetkezik == 'P' and not kov_allapot.piros:
            return 1
        if kov_allapot.kovetkezik == 'K' and not self.legalis_lepesek(kov_allapot):
            return 1
            
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'P', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás vagy nincs lehetséges lépés"""
        return allapot.eredmeny != 0 or not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        tabla = {}
        for mezo in allapot.piros:
            tabla[mezo] = 'P'
        for mezo in allapot.kek:
            tabla[mezo] = 'K'

        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
            )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = PirosKekKorong()

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: honnan_sor, honnan_oszl, hova_sor, hova_oszl | példa: 1,1,1,2\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
