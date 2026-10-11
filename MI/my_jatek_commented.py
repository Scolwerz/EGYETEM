from ast import literal_eval as make_tuple  # Sztring -> tuple konverzióhoz (pl. "(1,2)" -> (1,2))
import random  # Véletlenszám-generáláshoz (random_jatekos számára)


# ============================================================
# KIEGÉSZÍTŐ FÜGGVÉNYEK / OSZTÁLYOK
# ============================================================

def update(x, **entries):
    """Asszociatív tömb, struct értékeinek frissítése.
    Ha x szótár, az entries kulcs-érték párokat hozzáadja/frissíti.
    Ha x objektum, az attribútumait frissíti. Visszaadja a módosított x-et."""
    if isinstance(x, dict):     # Ha szótár típusú
        x.update(entries)       # Szótár kulcsait frissíti az entries-szel
    else:
        x.__dict__.update(entries)  # Objektum attribútumait frissíti
    return x  # Visszaadja a módosított objektumot (láncolt híváshoz)


def cmp(a, b):
    """Összehasonlítás: 1 ha a>b, -1 ha a<b, 0 ha egyenlők.
    Hasonló a régi Python 2-es cmp() beépített függvényéhez."""
    return (a > b) - (a < b)


def if_(test, result, alternative):
    """Háromágú értékadás (inline if-else).
    Ha a feltétel igaz, result-ot ad vissza, különben alternative-t.
    Ha valamelyik callable (hívható), akkor meghívja (lusta kiértékelés)."""
    if test:
        if callable(result):    # Ha függvény, hívja meg (lazy evaluation)
            return result()
        return result           # Ha nem függvény, adja vissza közvetlenül
    else:
        if callable(alternative):  # Ha függvény, hívja meg
            return alternative()
        return alternative         # Ha nem függvény, adja vissza közvetlenül


class Struct:
    """Pehelykönnyű, metódus nélküli adatstruktúra osztály.
    Névvel ellátott adatmezők tárolására, hasonló C-s struct-hoz."""

    def __init__(self, **entries):
        """Konstruktor: a kapott kulcsszavas argumentumokat attribútumként tárolja.
        Pl. Struct(x=1, y=2) -> s.x == 1, s.y == 2"""
        self.__dict__.update(entries)  # Minden kulcs-érték pár attribútum lesz

    def __repr__(self):
        """Szöveges megjelenítés hibakereséshez.
        Pl. Struct(x=1, y=2) formát ad vissza."""
        args = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return 'Struct(%s)' % ', '.join(args)


def jatssz(jatek, *jatekosok):
    """Általános n-személyes, felváltva lépő játékmenet vezérlő.
    Körönként minden játékos lép egyet, míg valamelyik nyeri vagy döntetlen."""
    allapot = jatek.kezdo    # Játék kezdőállapotának beállítása
    jatek.kiir(allapot)      # Kezdőállás megjelenítése
    while True:              # Körök végtelen ciklusa (a return állítja le)
        for jatekos in jatekosok:               # Minden játékos sorra kerül
            lepes = jatekos(jatek, allapot)     # Játékos választ egy lépést
            allapot = jatek.lep(lepes, allapot) # Lépést alkalmazza az állapotra
            jatek.kiir(allapot)                 # Frissített állás kiírása
            if jatek.levele(allapot):           # Ha terminális állapot (vége a játéknak)
                return jatek.hasznossag(allapot, jatekosok[0])  # Első játékos hasznosságát adja vissza


def num_or_str(x):
    """Lehetőség szerint számmá alakít, különben sztringet ad vissza.
    Először int-té próbálja, majd float-tá, végül str marad."""
    try:
        return int(x)      # Egész szám kísérlet
    except ValueError:
        try:
            return float(x)    # Lebegőpontos szám kísérlet
        except ValueError:
            return str(x).strip()  # Ha minden más sikertelen: szóköz-mentesített string


# ============================================================
# KERESÉSEK
# ============================================================

def minimax(allapot, jatek):
    """Legjobb lépés meghatározása teljes minimax kereséssel.
    Rekurzívan végigvizsgálja az összes lehetséges jövőbeli állást,
    és azt a lépést választja, ami maximalizálja az aktuális játékos nyereségét."""
    jatekos = jatek.kovetkezik(allapot)  # Aktuálisan lépő játékos azonosítása

    def max_ertek(allapot):
        """MAX játékos szintje: maximalizálja a hasznosságot.
        Terminális állapotban a tényleges hasznosságot adja vissza."""
        if jatek.levele(allapot):   # Ha a játék véget ért ennél az állapotnál
            return jatek.hasznossag(allapot, jatekos)  # Végeredmény értéke
        # Rekurzívan kiszámítja az összes rákövetkező állapot min-értékét, majd maximumot vesz
        return max([min_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])

    def min_ertek(allapot):
        """MIN játékos szintje: minimalizálja a hasznosságot (ellenfél lép).
        Terminális állapotban a tényleges hasznosságot adja vissza."""
        if jatek.levele(allapot):   # Ha a játék véget ért ennél az állapotnál
            return jatek.hasznossag(allapot, jatekos)  # Végeredmény értéke
        # Rekurzívan kiszámítja az összes rákövetkező állapot max-értékét, majd minimumot vesz
        return min([max_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])

    # A gyökér állapotból elérhető összes (lépés, értéke) pár kiszámítása
    fiai_ertekei = [(a, min_ertek(s)) for (a, s) in jatek.rakovetkezo(allapot)]
    # A maximális értékű lépés kiválasztása (az aktuális játékosnak legjobb)
    lepes, ertek = max(fiai_ertekei, key=lambda a_s: a_s[1])
    return lepes  # Visszaadja a legjobb lépés koordinátáját


def alfabeta_kereses(allapot, jatek, d=4, levagas_teszt=None, kiertekel=None):
    """Alfa-béta vágásos minimax keresés adott mélységig.
    Az alfa-béta vágás azonos eredményt ad, mint a minimax, de sokkal gyorsabb:
    felesleges ágakat levágja, ha azok biztosan nem befolyásolják az eredményt.
    d: maximális keresési mélység (alapértelmezés: 4 szint)"""
    jatekos = jatek.kovetkezik(allapot)  # Aktuálisan lépő játékos azonosítása

    def max_ertek(allapot, alfa, beta, melyseg):
        """MAX szint az alfa-béta keresésben.
        alfa: az eddigi legjobb érték MAX számára (alsó korlát)
        beta: az eddigi legjobb érték MIN számára (felső korlát)"""
        if levagas_teszt(allapot, melyseg):   # Mélységkorlát vagy terminális állapot
            return kiertekel(allapot)          # Heurisztikus értékelés
        v = float("-inf")  # MAX számára a legrosszabb kezdőérték
        for (a, s) in jatek.rakovetkezo(allapot):              # Minden lehetséges lépésre
            v = max(v, min_ertek(s, alfa, beta, melyseg+1))    # Rekurzív MIN hívás
            if v >= beta:   # Béta-vágás: MIN soha nem választaná ezt az ágat
                return v
            alfa = max(alfa, v)  # Alfa frissítése az új maximummal
        return v  # Legjobb érték ezen a MAX szinten

    def min_ertek(allapot, alfa, beta, melyseg):
        """MIN szint az alfa-béta keresésben.
        Szimmetrikus a max_ertek-kel, de minimalizálja az értéket."""
        if levagas_teszt(allapot, melyseg):   # Mélységkorlát vagy terminális állapot
            return kiertekel(allapot)          # Heurisztikus értékelés
        v = float("inf")   # MIN számára a legrosszabb kezdőérték
        for (a, s) in jatek.rakovetkezo(allapot):              # Minden lehetséges lépésre
            v = min(v, max_ertek(s, alfa, beta, melyseg+1))    # Rekurzív MAX hívás
            if v <= alfa:  # Alfa-vágás: MAX soha nem választaná ezt az ágat
                return v
            beta = min(beta, v)  # Béta frissítése az új minimummal
        return v  # Legjobb érték ezen a MIN szinten

    # Levágási teszt: alapértelmezés = mélységkorlát VAGY terminális állapot
    levagas_teszt = levagas_teszt or \
        (lambda allapot, melyseg: melyseg > d or jatek.levele(allapot))
    # Értékelő függvény: alapértelmezés = játék saját hasznosság-függvénye
    kiertekel = kiertekel or \
        (lambda allapot: jatek.hasznossag(allapot, jatekos))

    # Gyökér szintű keresés: manuálisan iterál az első szint lépésein
    alfa = float("-inf")  # Kezdeti alfa = -végtelen (MAX még semmit sem talált)
    legjobb_lepes = None  # Eddig még nincs legjobb lépés
    for a, s in jatek.rakovetkezo(allapot):      # Minden első szintű lépésre
        v = min_ertek(s, alfa, float("inf"), 0)  # MIN értéke az adott lépés után
        if v > alfa:         # Ha jobb az eddigi legjobbnál
            alfa = v         # Frissíti az alfa értéket
            legjobb_lepes = a  # Elmenti a legjobb lépést
    return legjobb_lepes  # Visszaadja a legjobb lépés koordinátáját


# ============================================================
# JÁTÉKOSOK
# ============================================================

def kerdez_jatekos(jatek, allapot):
    """Emberi játékos: billentyűzetről olvassa be a lépést.
    A num_or_str konvertálja a bemenet típusát (pl. "(1,2)" formátum)."""
    return num_or_str(input('Mit lép? '))


def random_jatekos(jatek, allapot):
    """Véletlenszerű stratégia: az összes legális lépés közül véletlenszerűen választ.
    Gyenge, de nem determinisztikus – tesztelési alap."""
    return random.choice(jatek.legalis_lepesek(allapot))


def alfabeta_jatekos(jatek, allapot):
    """Alfa-béta keresést alkalmazó gépi játékos.
    Korlátozott mélységű, de hatékony – erős az összetett játékokban."""
    return alfabeta_kereses(allapot, jatek)


def minimax_jatekos(jatek, allapot):
    """Teljes minimax keresést alkalmazó gépi játékos.
    Tökéletes TicTacToe-ban (kis fa), de nagyobb játékokban lassú."""
    return minimax(allapot, jatek)


# ============================================================
# JÁTÉK ALAPOSZTÁLY
# ============================================================

class Jatek:
    """Absztrakt alaposztály kétszemélyes, teljes információjú, nulla összegű játékokhoz.
    Ebből kell leszármaztatni a konkrét játékokat (pl. TicTacToe)."""

    def legalis_lepesek(self, allapot):
        """Adott állapotban megtehető legális lépések listája.
        Az utódosztálynak kötelezően felül kell definiálnia."""
        raise NotImplementedError()

    def lep(self, lepes, allapot):
        """Egy lépés végrehajtása: az aktuális állapotból új állapotot generál.
        Nem módosítja a meglévő állapotot (immutable), új Struct-ot ad vissza."""
        raise NotImplementedError

    def hasznossag(self, allapot, jatekos):
        """A terminális állapot értéke az adott játékos szempontjából.
        Pl. nyerés=+10, vesztés=-10, döntetlen=0."""
        raise NotImplementedError()

    def levele(self, allapot):
        """Igaz, ha az állapot terminális (a játék véget ért).
        Alapértelmezés: ha nincs több legális lépés, akkor vége."""
        return not self.legalis_lepesek(allapot)

    def kovetkezik(self, allapot):
        """A soron következő játékos azonosítója az állapotból.
        Az állapot tárolja, hogy ki következik ('X' vagy 'O')."""
        return allapot.kovetkezik

    def kiir(self, allapot):
        """Az aktuális állapot (tábla) szöveges megjelenítése a konzolon."""
        print(allapot)

    def rakovetkezo(self, allapot):
        """Az összes (lépés, rákövetkező állapot) pár listája.
        A keresési algoritmusok ezt hívják a fa bejárásához."""
        return [(lepes, self.lep(lepes, allapot))
                for lepes in self.legalis_lepesek(allapot)]

    def __repr__(self):
        """Játék osztályának neve szöveges formában (hibakereséshez)."""
        return '<%s>' % self.__class__.__name__


# ============================================================
# TIC-TAC-TOE OSZTÁLY
# ============================================================

class TicTacToe(Jatek):
    """Általánosított h×v-es amőba játék, ahol k db egymás melletti jel nyer.
    Alapértelmezés: 3×3-as tábla, 3-ban-egy nyerési feltétellel."""

    def __init__(self, h=3, v=3, k=3):
        """Játék inicializálása: tábla mérete h×v, k-ban-egy a nyerési feltétel.
        A kezdőállapot: X jön, nincs eredmény, üres tábla, minden mező szabad."""
        update(self, h=h, v=v, k=k)  # Táblaméret és nyerési feltétel tárolása
        # Összes lehetséges mező koordinátapárjainak generálása
        lepesek = [(x, y) for x in range(1, h+1) for y in range(1, v+1)]
        # Kezdőállapot Struct-ba csomagolva (immutable állapotkezelés)
        self.kezdo = Struct(
            kovetkezik='X',    # Az X játékos lép először
            eredmeny=0,        # Kezdetben nincs eredmény
            tabla={},          # Üres tábla (szótár: koordináta -> 'X'/'O')
            lepesek=lepesek    # Elérhető szabad mezők listája
        )

    def legalis_lepesek(self, allapot):
        """Minden üres mező (koordinátapár) lehetséges lépést jelent.
        Közvetlenül az állapotban tárolt szabad mezők listáját adja vissza."""
        return allapot.lepesek  # Üres mezők listája az állapotban

    def lep(self, lepes, allapot):
        """Egy lépés végrehajtása: az adott mezőre rakja az aktuális jelet.
        Új Struct-ot hoz létre (az eredeti állapot változatlan marad).
        Ha a lépés érvénytelen (nem üres mező), visszaadja az eredeti állapotot."""
        if type(lepes) is str:             # Ha szövegként jött (pl. "(1,2)")
            lepes = make_tuple(lepes)      # Tuple-vé alakítja
        if lepes not in allapot.lepesek:   # Érvénytelen lépés ellenőrzése
            return allapot                 # Változatlan állapot visszaadása

        tabla = allapot.tabla.copy()       # Tábla másolata (immutabilitás megőrzése)
        tabla[lepes] = allapot.kovetkezik  # Az aktuális játékos jelét rakja a mezőre

        lepesek = list(allapot.lepesek)    # Szabad mezők listájának másolata
        lepesek.remove(lepes)              # Az éppen betöltött mező törlése a szabadak közül

        # Új állapot visszaadása: ellenfél jön, frissített értékelés, módosított tábla
        return Struct(
            kovetkezik=if_(allapot.kovetkezik == 'X', 'O', 'X'),  # Játékosváltás
            eredmeny=self.ertekel(tabla, lepes, allapot.kovetkezik),  # Eredmény kiértékelése
            tabla=tabla,        # Frissített tábla
            lepesek=lepesek     # Csökkentett szabad mezők
        )

    def hasznossag(self, allapot, jatekos):
        """Az állapot értéke a megadott játékos szempontjából.
        X győz: +10, X veszít (O győz): -10, döntetlen: 0.
        Ha a 'jatekos' O, akkor az X eredményét negálja."""
        return if_(jatekos == "X", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Terminális állapot: valaki nyert (eredmény != 0) vagy megtelt a tábla.
        A nyerési értékelés után azonnal leáll a keresés."""
        return allapot.eredmeny != 0 or len(allapot.lepesek) == 0

    def kiir(self, allapot):
        """Az aktuális táblaállás megjelenítése sorokban, majd az eredmény kiírása.
        Üres mező: '.', X mező: 'X', O mező: 'O'."""
        tabla = allapot.tabla  # Az aktuális tábla referenciája
        for x in range(1, self.h+1):            # Sorokon végigmegy
            for y in range(1, self.v+1):        # Oszlopokon végigmegy
                print(tabla.get((x, y), '.'), end=" ")  # Mező tartalmát írja (vagy '.')
            print()          # Sor végén sortörés
        print(allapot.eredmeny)  # Aktuális eredmény kiírása (0, +10 vagy -10)
        print()              # Üres sor az olvashatóságért

    def ertekel(self, tabla, lepes, jatekos):
        """Heurisztikus értékelő függvény az utoljára megtett lépés után.

        Visszatérési értékek:
          +10 : ha az aktuális játékos (X) nyert ezzel a lépéssel
          -10 : ha az ellenfél (O) nyert
          0   : ha nincs nyertes, de vannak blokkolt sorok/oszlopok/átlók
                (a blokkolt irányok száma: 1-8 között)

        Blokkolt irány: egy sor/oszlop/átló, amelyet mindkét fél megjelölt
        (azaz egyik félnek sem lehet belőle nyerő sora).
        Ez a heurisztika segít az alfa-béta keresésnek jobb sorrendet felállítani
        a nem-terminális állapotokban is.
        """
        # --- Győzelem ellenőrzése (mind a 4 irányban) ---
        if (self.k_egy_sorban(tabla, lepes, jatekos, (0, 1)) or   # Vízszintes irány
                self.k_egy_sorban(tabla, lepes, jatekos, (1, 0)) or  # Függőleges irány
                self.k_egy_sorban(tabla, lepes, jatekos, (1, -1)) or # Mellékátló
                self.k_egy_sorban(tabla, lepes, jatekos, (1, 1))):   # Főátló
            # Ha X nyert: +10; ha O nyert: -10
            return if_(jatekos == 'X', +10, -10)

        # --- Nincs győzelem: blokkolt sorok számának kiszámítása ---
        # Blokkolt irányok száma (értéke: 0-8)
        blokkolt = self.blokkolt_iranyok_szama(tabla)

        # Az eredmény 0 (döntetlen-jellegű közbülső állapot),
        # de a blokkolt_iranyok tájékoztatnak a tábla "zártságáról"
        # Ezt az értéket az alfabeta_kereses heurisztikája tudja felhasználni
        return 0  # Terminális nem-nyerős esetekben (döntetlen vagy közbülső)

    def blokkolt_iranyok_szama(self, tabla):
        """Meghatározza, hogy hány sor/oszlop/átló blokkolt (1-8 közötti érték).

        Egy irány 'blokkolt', ha tartalmaz mind X-et, mind O-t,
        azaz egyik félnek sem lehet belőle nyerő sorozata.

        Ez heurisztikus információ: minél több blokkolt irány van,
        annál zártabb a tábla állása.
        """
        blokkolt = 0  # Blokkolt irányok számlálója

        # --- Vízszintes sorok vizsgálata (h db sor) ---
        for x in range(1, self.h + 1):          # Minden soron végigmegy
            mezok = [tabla.get((x, y)) for y in range(1, self.v + 1)]  # Sor mezői
            # Ha a sor tartalmaz X-et is és O-t is: blokkolt
            if 'X' in mezok and 'O' in mezok:
                blokkolt += 1

        # --- Függőleges oszlopok vizsgálata (v db oszlop) ---
        for y in range(1, self.v + 1):          # Minden oszlopon végigmegy
            mezok = [tabla.get((x, y)) for x in range(1, self.h + 1)]  # Oszlop mezői
            # Ha az oszlop tartalmaz X-et is és O-t is: blokkolt
            if 'X' in mezok and 'O' in mezok:
                blokkolt += 1

        # --- Főátló vizsgálata (bal felső -> jobb alsó) ---
        # Csak négyzetes táblán értelmezett (h == v eset)
        if self.h == self.v:  # Csak egyenlő oldalhosszú táblán vizsgáljuk
            fo_mezok = [tabla.get((i, i)) for i in range(1, self.h + 1)]
            if 'X' in fo_mezok and 'O' in fo_mezok:
                blokkolt += 1

        # --- Mellékátló vizsgálata (jobb felső -> bal alsó) ---
        # Csak négyzetes táblán értelmezett
        if self.h == self.v:  # Csak egyenlő oldalhosszú táblán vizsgáljuk
            mellyek_mezok = [tabla.get((i, self.v + 1 - i)) for i in range(1, self.h + 1)]
            if 'X' in mellyek_mezok and 'O' in mellyek_mezok:
                blokkolt += 1

        return blokkolt  # Visszaadja a blokkolt irányok számát (0-8 között)

    def k_egy_sorban(self, tabla, lepes, jatekos, irany):
        """Igaz, ha az adott lépéstől adott irányban (és ellentétes irányban)
        összesen legalább k azonos jel szerepel.

        Az irány egy (delta_x, delta_y) pár, pl.:
          (0, 1) = vízszintes
          (1, 0) = függőleges
          (1, 1) = főátló
          (1,-1) = mellékátló

        A függvény a lépés koordinátájától mindkét irányban számolja az egyforma jeleket,
        majd levonja 1-et, mert a kiindulópontot kétszer számolta.
        """
        delta_x, delta_y = irany  # Irányvektort kibontja
        x, y = lepes              # Kiindulópontot beállítja a lépés koordinátájára
        n = 0                     # Azonos jelek számlálója

        # Előre számolás (delta irányban)
        while tabla.get((x, y)) == jatekos:  # Amíg ugyanaz a jel szerepel
            n += 1               # Növeli a számlálót
            x, y = x + delta_x, y + delta_y  # Lép a következő mezőre

        # Visszaállás a lépés koordinátájára
        x, y = lepes

        # Hátra számolás (delta ellentétes irányában)
        while tabla.get((x, y)) == jatekos:  # Amíg ugyanaz a jel szerepel
            n += 1               # Növeli a számlálót
            x, y = x - delta_x, y - delta_y  # Lép a visszafelé következő mezőre

        n -= 1   # A lépés koordinátáját kétszer számoltuk, korrekció

        return n >= self.k  # Igaz, ha elérte a szükséges k hosszt


# ============================================================
# FŐPROGRAM
# ============================================================

def main():
    """Játék indítása: különféle játékos-kombinációk kipróbálása."""
    tto = TicTacToe()  # Alapértelmezett 3×3-as tábla, 3-ban-egy nyerési feltétel

    # Az alábbi kombinációk közül bármelyiket ki lehet kommentezni:

    # Két véletlen játékos egymás ellen
    # jatssz(tto, random_jatekos, random_jatekos)

    # X -> minimax_jatekos, O -> random_jatekos
    # jatssz(tto, minimax_jatekos, random_jatekos)

    # X -> random_jatekos, O -> minimax_jatekos
    # jatssz(tto, random_jatekos, minimax_jatekos)

    # Két minimax játékos egymás ellen (mindig döntetlen)
    # jatssz(tto, minimax_jatekos, minimax_jatekos)

    # X -> random_jatekos, O -> alfabeta_jatekos
    # jatssz(tto, random_jatekos, alfabeta_jatekos)

    # X -> alfabeta_jatekos, O -> random_jatekos
    # jatssz(tto, alfabeta_jatekos, random_jatekos)

    # Két alfabeta játékos egymás ellen (mindig döntetlen)
    jatssz(tto, alfabeta_jatekos,alfabeta_jatekos)

    pass  # Alapértelmezés: nem indul el automatikusan


if __name__ == '__main__':
    main()  # Közvetlen futtatáskor a main() hívódik meg