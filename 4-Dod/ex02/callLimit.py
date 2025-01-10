def callLimit(limit: int):
    """
    A decorator factory that limits the number
    of times a function can be called.
    Takes an integer 'limit' and ensures that
    the function will only be called
    up to that limit.
    """
    count = 0

    def callLimiter(function):
        """
        A decorator that applies the call limit
        logic to the provided function.
        Raises an error if the function is called
        more than the specified limit.
        """
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            try:
                if count >= limit:
                    raise AssertionError(
                        f"Error: {function} call too many times"
                    )
                count += 1
                return function(*args, **kwds)
            except AssertionError as e:
                print(e)
        return limit_function
    return callLimiter
