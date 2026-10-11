from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0,26)) + "\n")

def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
    return contents

def encrypt(message, key):
    ciphertext = ''
    for (position, character) in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext

def decrypt(ciphertext, key):
    neg_key = [int(x)*-1 for x in key]
    plaintext = encrypt(ciphertext, neg_key)
    return plaintext


def NODRYdecrypt(ciphertext, key):
    plaintext = ''
    for (position, character) in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(key[position])) % len(ALPHABET)
            plaintext += ALPHABET[decrypted]
    return plaintext


def main():
    message = input("Please enter a message to encrypt: ").lower()
    generate_otp(len(message))
    key = load_otp()

    encrypted_message = encrypt(message, key)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
