from ft_filter import ft_filter

def main():
    # A FUNCTION IS PROVIDED
    numbers = [1, 2, 3, 4, 5]
    even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
    print("Filtered even numbers:", even_numbers) 

    # None is provided
    values = [0, 1, False, 3, None, 5]
    truthy_values = ft_filter(None, values)
    print("Filtered truthy values:", truthy_values)



if __name__ == "__main__":
    main()