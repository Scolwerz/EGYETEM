#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    return ''.join(char for char in text if char in chars)

def main():
    print(valid("Barking!"))  # "B"
    print(valid("KL754", "0123456789"))  # "754"
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))  # ""
    

#############################################################################

if __name__ == "__main__":
    main()