import sys


def main():
    """
    Processes command-line arguments: filters words in the first argument
    based on length, using the second argument as the minimum length.
    Prints filtered words or error message if arguments are invalid.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        filtered = [word for word in sys.argv[1].split() if len(word) > num]
        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
