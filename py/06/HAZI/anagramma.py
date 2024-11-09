#!/usr/bin/env python3


def normalize(s):
    return ''.join(sorted(s.lower().replace(" ", "")))

def anagrams(s1, s2):
    return normalize(s1) == normalize(s2)


def main():
    print(anagrams("listen", "silent"))            # T
    print(anagrams("A gentleman", "Elegant man"))  # T
    print(anagrams("anagramma", "cipőfűző"))       # F


################################################################


if __name__ == '__main__':
    main()

