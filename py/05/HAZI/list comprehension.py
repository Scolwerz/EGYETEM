#!/usr/bin/env python3

def ex5():
"""
5. feladat
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak)
"""
input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
return = [int(x) for x in input]


def ex6():
"""
6. feladat
"1234567" → [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként)
"""
input = "1234567"
return = [int(x) for x in input]

def ex7():
"""
7. feladat
'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát
"""
input = 'The quick brown fox jumps over the lazy dog'
return = [len(word) for word in input.split()]

def ex8():
"""
8. feladat
"python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában
"""
input = "python is an awesome language"
return = [word[0] for word in input.split()]

def ex9():
"""
9. feladat
'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).
"""
input = 'The quick brown fox jumps over the lazy dog'
return = [(word, len(word)) for word in input.split()]

def ex10():
"""
10. feladat
[0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat
"""
return = [x for x in range(10) if x % 2 == 0]

def ex11():
"""
11. feladat
Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
"""
return = [x**2 for x in range(20) if (x**2) % 2 == 0]

def ex12():
"""
12. feladat
Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).
"""
return = [x**2 for x in range(20) if str(x**2)[-1] == '4']

def ex13():
"""
13. feladat
Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
"""
return = ''.join([chr(x) for x in range(int('A'), int('Z')+1])

def ex14():
"""
14. feladat
[' apple ', ' banana ', ' kiwi'] → ['apple', 'banana', 'kiwi'], vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket
"""
input = [' apple ', ' banana ', ' kiwi']
return = [word.strip() for word in input]

def ex15():
"""
15. feladat
[1, 0, 1, 1, 0, 1, 0, 0] → "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé
"""
input = [1, 0, 1, 1, 0, 1, 0, 0]
return = ''.join([str(x) for x in input])



def main():
    print("5. feladat:", ex5())
    print("6. feladat:", ex6())
    print("7. feladat:", ex7())
    print("8. feladat:", ex8())
    print("9. feladat:", ex9())
    print("10. feladat:", ex10())
    print("11. feladat:", ex11())
    print("12. feladat:", ex12())
    print("13. feladat:", ex13())
    print("14. feladat:", ex14())
    print("15. feladat:", ex15())



#############################################################################

if __name__ == "__main__":
    main()
