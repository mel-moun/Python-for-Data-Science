def ft_tqdm(lst: range) -> None:
    """
    Simulates a progress bar for iterating over a list.

    Args:
    - lst: A list or range to iterate over.

    Yields:
    - Each item from the list during iteration.

    Displays the progress bar in the console.
    """
    total = len(lst)
    bar_length = 135

    for i, item in enumerate(lst):
        progress = (i + 1) / total
        filled_length = int(progress * bar_length)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        percent = f'{progress*100:.0f}%'
        print(f'\r{percent}|{bar}| {i+1}/{total}', end='', flush=True)

        yield item

    print(f'\r100%|{"█" * bar_length}| {total}/{total}')
