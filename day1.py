import re
from typing import Tuple, List

FILEPATH = "day-1-input.txt"

def read_file(filepath: str = FILEPATH) -> str:
    """Reads a text file into memory.

    Parameters
    ----------
    filepath : str, optional
        The filepath to read, by default FILEPATH

    Returns
    -------
    str
        The text string contained in the text file.
    """

    f = open(filepath)
    text = f.read()
    f.close()

    return text

def convert_string_to_lists(string: str, sort: bool = False) -> Tuple[List, List]:
    """Converts a Day-1-formatted text string into two lists

    Parameters
    ----------
    string : str
        the text string to format
    sort : bool, optional
        whether to return two sorted lists, by default False

    Returns
    -------
    Tuple[List, List]
        a tuple containing the two lists
    """

    split_str = re.split(r'\D+', string)

    lists = (list(), list())

    for idx, value in enumerate(split_str):
        list_idx = idx % 2
        if value:
            lists[list_idx].append(int(value))
    
    assert len(lists[0]) == len(lists[1])

    if sort:
        lists[0].sort()
        lists[1].sort()

    return lists

def read_lists(filepath: str = FILEPATH, sort: bool = False) -> Tuple[List, List]:
    """wrapper to read the text file & convert to a list

    Parameters
    ----------
    filepath : str, optional
        filepath to read in, by default FILEPATH
    sort : bool, optional
        whether to sort the lists, by default False

    Returns
    -------
    Tuple[List, List]
        a tuple containing the two lists
    """

    raw_text = read_file(filepath=filepath)
    lists = convert_string_to_lists(string=raw_text, sort=sort)
    return lists

lists = read_lists(sort=True)

# Part I solution ----
distance = 0

# loop over & sum the element-wise difference between the lists
for idx, _ in enumerate(lists[0]):
    distance += abs(lists[0][idx] - lists[1][idx])

print(f"Distance between lists: {distance}")

# Part II solution ----
similarity = 0

# first, get how many times each list-1 element is in list 2
counts = list()
for value in lists[0]:
    counts.append(lists[1].count(value))

# then, calculate the similarity score for each value in the 1st list
for idx, value in enumerate(lists[0]):
    similarity += value * counts[idx]

print(f"Similarity score: {similarity}")