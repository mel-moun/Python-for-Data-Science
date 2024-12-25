import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    i = 0
    bar_length = 200
    for item in lst:
        progress = (i + 1) / total

        filled_length = int(progress * bar_length)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        percent = f'{progress*100:.0f}%'

        sys.stdout.write(f'\r{percent}|{bar}| {i+1}/{total}')
        sys.stdout.flush()

        yield item

        i += 1

    sys.stdout.write(f'\r100%|{"█" * bar_length}| {total}/{total}\n')
    sys.stdout.flush()
