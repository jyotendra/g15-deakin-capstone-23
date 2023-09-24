from itertools import islice

def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def print_spaced(title, body, footer=None):
    """
    print with proper spacing and newlines
    """
    print(f"\n{title}")
    print(body)
    if footer:
        print(footer)
    print("\n")