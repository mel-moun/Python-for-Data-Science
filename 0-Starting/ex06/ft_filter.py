def ft_filter(function, iterable):
    """
    Filters elements from iterable based on function. 
    If function is None, removes falsy values.

    Args:
    - function: Function to test elements, or None.
    - iterable: Iterable to filter.

    Returns:
    - List of filtered elements.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
