#!/usr/bin/env python3


class MyQueue:
    def __init__(self):
        self.verem1 = []
        self.verem2 = []

    def append(self, elem):
        self.verem1.append(elem)

    def popleft(self):
        if not self.verem2:
            while self.verem1:
                self.verem2.append(self.verem1.pop())
        if self.verem2:
            return self.verem2.pop()
        else:
            return None

    def is_empty(self):
        return len(self.verem1) + len(self.verem2) == 0

    def size(self):
        return len(self.verem1) + len(self.verem2)

    def __str__:
        return '[' + ' '.join(str(elem) for elem in self.verem1) + ' '.join(str(elem) for elem in self.verem2) ']'


def main():
    # Teszteljük az osztályt
    q = MyQueue()
    print(q.is_empty())  # True
    print(q)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    print(q.size())      # 3
    print(q.popleft())   # 1
    print(q)
    print(q.popleft())   # 2
    print(q.is_empty())  # False
    print(q.popleft())   # 3
    print(q.is_empty())  # True
    print(q.popleft())   # None (üres sorból való kivétel)


#############################################################################

if __name__ == "__main__":
    main()