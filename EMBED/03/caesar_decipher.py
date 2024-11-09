#iqfihhih

def caesar_decryption(msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(1, 26):
        decry_message = ""
        for c in msg:
            position = alphabet.find(c)
            new_position = (position - key) % len(alphabet)
            new_character = alphabet[new_position]
            decry_message += new_character
        print(f"Key: {key} - {decry_message}")
    return


def main():
    encry_message = input("Please enter a coded message: ")
    caesar_decryption(encry_message)


if __name__ == "__main__":
    main()
