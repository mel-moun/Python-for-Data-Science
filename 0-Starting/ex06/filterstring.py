from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        filtered = ft_filter(lambda word: len(word) > num, sys.argv[1].split())
        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
