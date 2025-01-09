def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    result = x

    def inner() -> float:
        nonlocal result
        result = function(result)
        return result

    return inner
