morse_codes = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }


def decode_morse(message):
    words = message.split(' / ')

    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(morse_codes[letter] for letter in letters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


def main():
    message = ". -- -... . -.. -.. . -.. / ... -.-- ... - . -- ..."
    print(decode_morse(message))


if __name__ == "__main__":
    main()