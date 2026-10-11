def caesar(msg, key):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = ""
    for c in msg:
        if c in lower_alphabet:
            position = lower_alphabet.find(c)
            new_position = (position + key) % len(lower_alphabet)
            new_character = lower_alphabet[new_position]
            new_message += new_character
        elif c in upper_alphabet:
            position = upper_alphabet.find(c)
            new_position = (position + key) % len(upper_alphabet)
            new_character = upper_alphabet[new_position]
            new_message += new_character
        else:
            new_message += c
    return new_message


def main():
    key = 3
    while True:
        message = input("Please enter a message: ")
        if message == 'q': break
        encry_message = caesar(message, key)
        print("Encrypted message:", encry_message)
        decry_message = caesar(encry_message, -key)
        print("Decrypted message:", decry_message)


if __name__ == "__main__":
    main()
