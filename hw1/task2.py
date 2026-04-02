"""
CMSC 14200, Spring 2026
Homework 1, Task 2

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


def affordable_subsequences(budget: int, ints: list[int]) -> list[list[int]]:
    """
    This function will return subsequences of the input list whose combined
    sum is <= to the given budget, making it "affordable". My function
    approaches it recursively, considering the option to include the first
    element or to exclude it, so every combination is scanned up until the
    entire list for each combination is scanned through.

    Args:
        budget (int): The budget value that the subsequences cannot exceed.
            Assumed to non-negative.
        ints (list[int]): The input list of which I am trying to find
            subsequences of. Assumed that each list contains only non-negative
            numbers, and is without duplicates.

    Returns (list[list[int]]): Affordable subsequences. Can appear in any order
    """
    if len(ints) == 0:
        return [[]]
    fst = ints[0]
    rst = ints[1:]
    subseq_without = affordable_subsequences(budget,rst)
    subseq_with = []
    if fst <= budget:
        remaining = affordable_subsequences(budget - fst, rst)
        for sub in remaining:
            subseq_with.append([fst] + sub)
    return subseq_without + subseq_with


   
