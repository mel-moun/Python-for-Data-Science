def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if not args:
            raise AssertionError("ERROR") 

        for x, val in kwargs.items():
            if val == 'mean':
                print(val, ":", ft_mean(args))
            elif val == 'median':
                print(val, ':', ft_median(args))
            elif val == 'quartile':
                print(val, ':', ft_quartile(args))
            else:
                raise AssertionError("ERROR")

    except AssertionError as e:
        print(e)
    
def ft_mean(args):
    return sum(args) / len(args)


def ft_median(args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    
    if n % 2 == 1:
        median = sorted_args[n // 2]
    else:
        mid1 = sorted_args[n // 2 - 1]
        mid2 = sorted_args[n // 2]
        median = (mid1 + mid2) / 2
    
    return median


def ft_quartile(args):
    list_n = list(args)
    list_n.sort()
    median = ft_median(list_n)

    one = ft_median(filter(lambda x: x <= median, list_n))
    two = ft_median(filter(lambda x: x >= median, list_n))

    return [one, two]
