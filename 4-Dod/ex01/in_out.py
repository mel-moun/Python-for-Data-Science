def square(x: int | float) -> int | float:
    """
    Returns the square of the given number (x).
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns x raised to the power of x (x^x).
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function that applies
    the given function to x and updates its result.
    The inner function, when called, will modify
    the value of x based on the provided function.
    The result will be accumulated and returned each
    time the inner function is called.
    """
    count = 0

    def inner() -> float:
        """
        Applies the function to the current value
        of count (or x initially) and updates count.
        The inner function, when called,
        will return the updated result after applying
        the provided function to it.
        """
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count

    return inner
