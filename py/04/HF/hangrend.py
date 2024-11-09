#!/usr/bin/env python3


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def hangrend(word):
    mely_mghk_count = sum(1 for c in word if c in MELY_MGHK)
    magas_mghk_count = sum(1 for c in word if c in MAGAS_MGHK)

    if mely_mghk_count > 0 and magas_mghk_count == 0:
        return "mély"
    elif mely_mghk_count == 0 and magas_mghk_count > 0:
        return "magas"
    elif mely_mghk_count > 0 and magas_mghk_count > 0:
        return "vegyes"
    else:
        return "semmilyen"

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for word in words:
        print(f"{word}: {hangrend(word)}")

#############################################################################

if __name__ == "__main__":
    main()
