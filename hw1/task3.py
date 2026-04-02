"""
CMSC 14200, Spring 2026
Homework 1, Task 3

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


def merge_dictionaries(dicts: list[dict[str, int]]) -> dict[str, list[int]]:
    """
    Merge a list of dictionaries into a single dictionary, where each key maps
    to a list of distinct values for that key in all of the input dictionaries.
    My approach creates a new dictionary, and adds keys and values if the key
    is not present, but if the key is present and the value is not, it will
    append the value to the existent key.
    
    Args:
        dicts (list[dict[str,int]]): a list of dictionaries that will be merged

    Returns (dict[str, list[int]]): a dictionary where the value of each key
            is a list of DISTINCT values for said key
    """
    out = {}
    for d in dicts:
        for key, val in d.items():
            if key not in out:
                out[key] = [val]
            elif val not in out[key]:
                out[key].append(val)
    return out


