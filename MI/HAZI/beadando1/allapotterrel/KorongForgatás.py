from keres import *

# Legyen N ∈ ℕ⁺ a korongok száma. A korongokat 1..N egészekkel jelöljük,
# ahol 1 a legkisebb és N a legnagyobb.
#
# ÁLLAPOTTÉR
# -----------
# Egy állapot az oszlopon lévő korongok sorrendjét írja le fentről lefelé:
#   S = (s₁, s₂, ..., sₙ) ∈ Perm({1,...,N})
# ahol sᵢ az i-edik pozícióban (fentről) lévő korong mérete.
#
# KEZDŐÁLLAPOT
# ------------
# A képen látható kezdeti permutáció (N=8 esetén):
#   s₀ = (6, 7, 3, 2, 8, 5, 4, 1)
#
# Általánosan: tetszőleges permutáció adható meg.
#
# CÉLÁLLAPOT
# ----------
# A korongok nagység szerint rendezve, legfelül a legkisebb:
#   s* = (1, 2, 3, ..., N)
#
# Formálisan: s* olyan permutáció, ahol ∀i < j : s*ᵢ < s*ⱼ
#
# OPERÁTOROK HALMAZA
# ------------------
# Az operátorok halmaza:
#   O = { op(k) | k ∈ {1, 2, ..., N} }
#
# ahol op(k) jelenti: "emeld le a tetőről a felső k korongot,
# fordítsd meg a sorrendjüket, majd helyezd vissza"
#
# Ekvivalensen:
#   op(k) : (s₁,...,sₙ) → (sₖ, sₖ₋₁, ..., s₁, sₖ₊₁, ..., sₙ)
#
# Megjegyzés: op(1) az identitás (egy korongot megfordítva visszarakni),
# de nem zárjuk ki, mert a gráfkereső kezeli a ciklust.
#
# OPERÁTOR ALKALMAZÁSI ELŐFELTÉTELE
# ----------------------------------
# Pre(op(k), s) = (1 ≤ k ≤ N)
#
# Azaz minden k ∈ {1,...,N} esetén az operátor mindig alkalmazható
# (nincs méret-korlát a felemelésre, és visszarakáskor a sorrend megfordul).
# Az egyetlen feltétel, hogy k érvényes index legyen.
#
# OPERÁTOR ALKALMAZÁSI FÜGGVÉNYE
# --------------------------------
# γ(op(k), s) = (sₖ, sₖ₋₁, ..., s₁, sₖ₊₁, ..., sₙ)
#
# Halmazelméleti jelöléssel, ha s = (s₁,...,sₙ) ∈ Perm({1,...,N}), akkor:
#   γ(op(k), s)ᵢ = sₖ₋ᵢ₊₁    ha  1 ≤ i ≤ k
#   γ(op(k), s)ᵢ = sᵢ         ha  k < i ≤ N
#
# HEURISZTIKA
# -----------
# h(s) = az a legnagyobb index j, amelyre s[j-1..N-1] már rendezett
#         (azaz az alulról már a helyükön lévő korongok száma).
# Pontosabban: h(s) = N - (azon i értékek száma, ahol s[i] = i+1 és
#              minden j > i esetén is s[j] = j+1)
# Ez egy elfogadható (admissible) heurisztika.
# =============================================================================


class KorongForgatás(Feladat):
    def __init__(self, kezdő):
        self.kezdő = kezdő
        self.N = len(kezdő)
        self.cél = tuple(range(1, self.N + 1))

    def célteszt(self, a):
        return a == self.cél

    def rákövetkező(self, a):
        gyerekek = []
        lista_állapot = list(a)
        for k in range(1, self.N + 1):
            új_állapot = lista_állapot[:k][::-1] + lista_állapot[k:]
            gyerekek.append((f"forgat({k})", tuple(új_állapot)))
        return gyerekek


def heurisztika(csúcs):
    a = csúcs.állapot
    n = len(a)
    már_rendezett = 0
    for i in range(n - 1, -1, -1):
        if a[i] == i + 1:
            már_rendezett += 1
        else:
            break
    return n - már_rendezett


if __name__ == '__main__':
    kezdő = (6, 7, 3, 2, 8, 5, 4, 1)

    feladat1 = KorongForgatás(kezdő)
 
    print("\nbest_first (heurisztikával):")
    result1 = best_first(feladat1, heurisztika)
    print(f"Lépések: {result1.megoldás()}")

    print("\nszélességi_gráfkereső:")
    result2 = szélességi_gráfkereső(feladat1)
    print(f"Lépések: {result2.megoldás()}")
