# tools/col.py

def myzip(it1, it2):
    """
    Custom implementation of zip function for two collections.

    Args:
    - it1 (iterable): First iterable to zip.
    - it2 (iterable): Second iterable to zip.

    Returns:
    - list: A list of tuples where each tuple contains elements from it1 and it2.
    """
    min_len = min(len(it1), len(it2))
    return [(it1[i], it2[i]) for i in range(min_len)]
