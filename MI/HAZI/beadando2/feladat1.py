from my_jatek import *

def alap_foglalt_mezok(meret):
    piros = [(i, j) for i in range(meret) for j in range(meret) if i % 2 == 1 and j % 2 == 0]
    kek = [(i, j) for i in range(meret) for j in range(meret) if i % 2 == 0 and j % 2 == 1]
    return piros, kek

def osszes_mezo(meret):
    return [(sor, oszlop) for sor in range(meret) for oszlop in range(meret)]
    

class TablaSzinezes(Jatek):
    def __init__(self, meret=11):
        self.N = meret
        
        piros, kek = alap_foglalt_mezok(meret)
        foglalt = set(piros) | set(kek)
        
        lepesek = [mezo for mezo in osszes_mezo(meret) if mezo not in foglalt]

        self.kezdo = Struct(
            kovetkezik='K',     # kék kezd
            tabla={mezo: 'P' for mezo in piros} | {mezo: 'K' for mezo in kek},
            lepesek=lepesek,
            eredmeny=0      # 0 = folyamatban, 1 = K nyert, -1 = P nyert
        )

    def legalis_lepesek(self, allapot):
        """
        Lépés: (sor, oszlop)
        """
        return allapot.lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in allapot.lepesek:
            return allapot   # téves lépés

        tabla = allapot.tabla.copy()
        tabla[lepes] = allapot.kovetkezik
        lepesek = list(allapot.lepesek)
        lepesek.remove(lepes)

        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'K', 'P', 'K'),
            tabla=tabla,
            lepesek=lepesek,
            eredmeny=self.ertekel(tabla, allapot.kovetkezik) )

    def ertekel(self, tabla, jatekos):
        n = self.N

        if jatekos == 'K':
            for j in range(n):
                if all(tabla.get((i, j)) == 'K' for i in range(n)):
                    return 1
        else: # 'P'
            for i in range(n):
                if all(tabla.get((i, j)) == 'P' for j in range(n)):
                    return -1
        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == 'K', allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Nyert állás vagy a tele tábla"""
        return allapot.eredmeny != 0 or not allapot.lepesek

    def kiir(self, allapot):
        print("  " + " ".join(str(oszl) for oszl in range(self.N)))  # header
        for sor in range(self.N):
            print(str(sor) + " " +
                  " ".join(allapot.tabla.get((sor, oszlop), '_') for oszlop in range(self.N))
                  )

        print(f"Következik: {allapot.kovetkezik}   Eredmény: {allapot.eredmeny}")
        print()


if __name__ == '__main__':
    jatek = TablaSzinezes(meret=4)  

    jatssz(jatek, alfabeta_jatekos, random_jatekos)
    print("\n\ninput: sor,oszlop | példa: 1,1\n")
    jatssz(jatek, random_jatekos, kerdez_jatekos)
