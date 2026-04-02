"""
CMSC 14200, Spring 2026
Homework 1, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

   Jack Kozlowski - I didn't have access to the HW so asked him for the files

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def to_base_n(n: int, num: int) -> str:
    """
    Returns a nitstring of the format "0_b_nits", where b is the base and
    nits is a string of one or more characters, each between 0 and the symbol
    representing b-1. My methodology involves finding the highest power,
    determining how many will fit within that power, and keeping the leftovers
    to the determine the same for the next highest power until the 0th power
    is reached (rightmost digit).

    Args:
        n (int): the base
        num (int): the number that will be represented by the bases

    Returns (str): "0_b_nits", where b is the base and nits is a string of
            characters, where each character is the quantity of representations
            needed of b^n ... b^2, b^1, b^0.
    """
    if num == 0:
        return f"0_{n}_0"
    highest_power = 0
    while n ** (highest_power + 1) <= num:
        highest_power = highest_power + 1
    nits = ""
    remaining = num
    for power in range(highest_power, -1, -1):
        digit = remaining // (n ** power)
        nits = nits + str(digit)
        remaining = remaining % (n ** power)
    return f"0_{n}_{nits}"


def from_base_n(s: str) -> int:
    """
    Takes the nitstring in the format "0_b_nits" where b is the base and
    nits is a string of one or more characters, each between 0 and the symbol
    representing b-1, and subsequently returns the number that it is storing.
    """
    parts = s.split("_")
    
    base = int(parts[1])
    nits = parts[2]
    reverse_nits = nits[::-1]
    
    num = 0
    for i in range(len(reverse_nits)):
        digit = int(reverse_nits[i])
        num = num + digit * (base ** i)
    return num