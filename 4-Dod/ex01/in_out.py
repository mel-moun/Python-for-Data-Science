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
    Returns an inner function that applies the given
    function to x and updates its result.
    The inner function, when called, will modify
    the value of x.
    """
    result = x

    def inner() -> float:
        nonlocal result
        result = function(result)
        return result

    return inner
