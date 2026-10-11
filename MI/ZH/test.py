

def fakereső(feladat, perem):
    perem.append(Csúcs(feladat.kezdő))
    while perem:
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        else:
            perem.extend(csúcs.kiterjeszt(feladat))

    return None


def gráfkereső(feladat, perem):
    kifejtési_sor = set()
    perem.append(Csúcs(feladat.kezdő))
    while perem:
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        if csúcs.állapot not in kifejtési_sor:
            kifejtési_sor.add(csúcs.állapot)
            perem.extend(csúcs.kiterjeszt(feladat))
    return None

def szélességi_fakereső(feladat):       return fakereső(feladat,Sor())
def mélységi_fakereső(feladat):         return fakereső(feladat,Verem())
def szélességi_gráfkereső(feladat):     return gráfkereső(feladat, Sor())
def mélységi_gráfkereső(feladat):       return gráfkereső(feladat, Verem())
def best_first(feladat, heurisztika):   return gráfkereső(feladat,RendezettLista(heurisztika))
def a_csillag(feladat, heurisztika):
    def f(csúcs):
        return csúcs.útköltség + heurisztika(csúcs)
    return best_first(feladat,f)


def minimax(allapot, jatek):
    jatekos = jatek.kovetkezik(allapot)

    def max_ertek(allapot):
        if jatek.levele(allapot):
            return jatek.hasznossag(allapot, jatekos)
        return max([min_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])
    
    def min_ertek(allapot):
        if jatek.levele(allapot):
            return jatek.hasznossag(allapot, jatekos)
        return min([max_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])

    fiai_ertekei = [(a, min_ertek(s)) for (a, s) in jatek.rakovetkezo(allapot)]
    lepes, ertek = max(fiai_ertekei, key=lambda a_s: a_s[1])
    return lepes


def alfabeta_kereses(allapot, jatek, d=4, levagas_teszt=None, kiertekel=None):
    jatekos = jatek.kovetkezik(allapot)

    def max_ertek(allapot, alfa, beta, melyseg):
        if levagas_teszt(allapot, melyseg):
            return kiertekel(allapot)
        v = float("-inf")
        for (a, s) in jatek.rakovetkezo(allapot):
            v = max(v, min_ertek(s, alfa, beta, melyseg+1))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        return v
    
    def min_ertek(allapot, alfa, beta, melyseg):
        if levagas_teszt(allapot, melyseg):
            return kiertekel(allapot)
        v = float("inf")
        for (a, s) in jatek.rakovetkezo(allapot):
            v = min(v, max_ertek(s, alfa, beta, melyseg+1))
            if v <= alfa:
                return v
            beta = min(beta, v)
        return v

    levagas_teszt = levagas_teszt or \
        (lambda allapot, melyseg: melyseg > d or jatek.levele(allapot))
    kiertekel = kiertekel or \
        (lambda allapot: jatek.hasznossag(allapot, jatekos))
    alfa = float("-inf")
    legjobb_lepes = None
    for a, s in jatek.rakovetkezo(allapot):
        v = min_ertek(s, alfa, float("inf"), 0)
        if v > alfa:
            alfa = v
            legjobb_lepes = a
    return legjobb_lepes







if __name__ == '__main__':
    pass
    