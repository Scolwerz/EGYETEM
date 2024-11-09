#!/usr/bin/env python3



def is_valid_passphrase(phrase):
    words = phrase.split()
    words_set = set(words)
    return len(words_set) == len(words)


def valid_passphrases_count(passphrases):
    count = 0
    for phrase in passphrases:
        if is_valid_passphrase(phrase):
            count += 1
    return count


def main():
    with open('input.txt', 'r') as file:
        for line in file:
            szavak += line.strip()

    print("Érvényes jelmondatok száma:", valid_passphrases_count(szavak))


################################################################


if __name__ == '__main__':
    main()
    