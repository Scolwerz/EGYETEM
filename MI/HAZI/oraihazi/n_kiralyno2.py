class Kiralyno:
    def __init__(self, ke, c, n):
        self.kezdo = ke
        self.cel = c
        self.n = n

    def celteszt(self, a):
        return a == self.cel

    def rakovetkezo(self, a):
        gyerekek = []

        sor = -1
        for s in range(self.n):
            if 1 not in a[s]:
                sor = s
                break
        if sor == -1:   # minden sorban van q
            return gyerekek

        for oszlop in range(self.n):
            elofeltetel = True

            # oszlop
            for i in range(sor):
                if a[i][oszlop] == 1:
                    elofeltetel = False
                    break

            # bal felső átló
            i = sor - 1
            j = oszlop - 1
            while i >= 0 and j >= 0:
                if a[i][j] == 1:
                    elofeltetel = False
                    break
                i -= 1
                j -= 1

            # jobb felső átló
            i = sor - 1
            j = oszlop + 1
            while i >= 0 and j < self.n:
                if a[i][j] == 1:
                    elofeltetel = False
                    break
                i -= 1
                j += 1


            if elofeltetel:
                uj_allapot = [row[:] for row in a]
                uj_allapot[sor][oszlop] = 1
                gyerekek.append(uj_allapot)

        return gyerekek



if __name__ == "__main__":
    n = 4
    kezdo = [[0] * n for _ in range(n)]
    cel = [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]
    feladat = Kiralyno(kezdo, cel, n)
