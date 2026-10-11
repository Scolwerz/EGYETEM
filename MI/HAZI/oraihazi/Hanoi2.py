class Hanoi:
    def __init__(self, ke, c):
        self.kezdo = ke # ([1,2,3,4], [], [])
        self.cel = c    # [], [], [1,2,3,4])
        self.N = sum(len(rud) for rud in ke)

    def celteszt(self, a):
        return a == self.cel

    def rakovetkezo(self, a):   # a=([p1,p2,...,pk],[q1,q2,...,ql],[r1,r2,...,rj])  |  {p1,p2,...,pk} U {q1,q2,...,ql} U {r1,r2,...,rj} = {1,2,...,n}
        gyerekek = []

        for honnan in range(3): # 0=P 1=Q 2=R
            if len(a[honnan]) != 0:
                for hova in range(3):
                    if honnan != hova and ( len(a[hova]) == 0 or a[hova][0] > a[honnan][0] ):   # teljesül minden feltétel
                        gyerek_allapot = [ a[0].copy(), a[1].copy(), a[2].copy() ]
                        gyerek_allapot[honnan].pop(0)
                        gyerek_allapot[hova].insert(0, a[honnan][0])
                        gyerekek.append(tuple(gyerek_allapot))
        return gyerekek


if __name__ == '__main__':
    feladat = Hanoi( ([1,2,3,4], [], []), ([], [], [1,2,3,4]) )
