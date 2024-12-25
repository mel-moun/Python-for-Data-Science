import sys


def to_morse(string) -> str:
    NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
    }

    string = string.upper()
    encoded = []
    for char in string:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        encoded.append(NESTED_MORSE[char])
    return ' '.join(encoded)

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        encoded = to_morse(sys.argv[1])
        print(encoded)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == '__main__':
    main()
