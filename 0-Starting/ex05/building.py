import sys

def get_input() -> str:
    """ Prompts the user for input and returns the input string.
    Keeps asking until a non-empty string is entered. """

    while True:
        try:
            user_input = input("What is the text to count?\n")
            if user_input:
                return user_input
        except (EOFError, KeyboardInterrupt):
            return ""

def sum_characters(string):
    """ Analyzes the given string and counts the number of uppercase letters,
    lowercase letters, punctuation marks, digits, and spaces.
    Then, prints the total character count and the count of each category."""

    upper = 0
    lower = 0
    punct = 0
    digits = 0
    spaces = 0
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

    for x in string:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x in punctuation:
            punct += 1
        elif x.isdigit():
            digits += 1
        elif x.isspace():
            spaces += 1
    
    total = len(string)
    print("The text contains", total, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")

def main():
    """ Main function to handle input and call the analysis function.
    It checks the number of command-line arguments.
    If no arguments are passed, it prompts the user for input.
    If an argument is provided, it uses that as the input.
    Calls the sum_characters function to analyze the text. """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
     
        if len(sys.argv) == 1:
            user_input = get_input()
        else:
            user_input = sys.argv[1]

        if (user_input):
            sum_characters(user_input)

    except Exception as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
