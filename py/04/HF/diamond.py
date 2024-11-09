#!/usr/bin/env python3


def draw_diamond(height):
    if height % 2 == 0:
        print("Hiba: Csak páratlan magasság adható meg!")
        return
    
    for i in range(1, height + 1):
        if (i <= (height + 1) // 2):
            spaces = " " * ((height - i) // 2)
            stars = "*" * i
        else:
            spaces = " " * ((i - 1) // 2)
            stars = "*" * (height - i + 1)
        print(spaces + stars.center(height))


def main():
    draw_diamond(3)
    draw_diamond(9)
    draw_diamond(8)


#############################################################################

if __name__ == "__main__":
    main()
    



