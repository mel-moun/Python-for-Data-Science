def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if not args:
            raise AssertionError("ERROR") 

        for x, val in kwargs.items():
            if val == 'mean':
                ft_mean(args)
            elif val == 'median':
                ft_median(args)

    except AssertionError as e:
        print(e)
    
def ft_mean(args):
    print("sum :", sum(args) / len(args))


def ft_median(args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    
    if n % 2 == 1:
        median = sorted_args[n // 2]
    else:
        mid1 = sorted_args[n // 2 - 1]
        mid2 = sorted_args[n // 2]
        median = (mid1 + mid2) / 2
    
    print("median :", median)
