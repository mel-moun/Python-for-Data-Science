def ft_statistics(*args: any, **kwargs: any) -> None:
    op = {
        'mean': ft_mean,
        'median': ft_median,
        'quartile': ft_quartile,
        'std': ft_std,
        'var': ft_var,
    }

    try:
        for _, value in kwargs.items():
            if value in op.keys():
                if len(args) > 0:
                    print(value, ':', op[value](args))
                else:
                    print('ERROR')

    except BaseException as e:
        print(type(e).__name__, ':', e)


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


def ft_std(args):
    var = ft_var(args)
    return var ** 0.5


def ft_var(args):
    mean = ft_mean(args)
    return sum((x - mean) ** 2 for x in args) / len(args)
