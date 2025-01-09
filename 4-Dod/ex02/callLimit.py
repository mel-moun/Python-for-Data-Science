def callLimit(limit: int):
    count = 0

    def callLimiter(function):
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
