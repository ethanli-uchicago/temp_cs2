"""
CMSC 14200, Spring 2026
Homework 1, Extra Tests
"""

import pytest

import task1
import task2
import task3
from task4 import Card


## TASK 1
def test_task1_to_base_2_250() -> None:
    assert task1.to_base_n(2, 250) == "0_2_11111010"

def test_task1_from_base_9_000843() -> None:
    assert task1.from_base_n("0_9_000843") == 687

## TASK 2
def assert_equal_task2(list1: list[list[int]], list2: list[list[int]]) -> None:
    list1.sort()
    list2.sort()
    assert list1 == list2

@pytest.mark.parametrize(
    "budget, ints, expected",
    [
        (
            6, 
            [2, 4, 6], 
            [[], [2], [4], [6], [2, 4]]
        ),
        (
            10,
            [1, 9, 11],
            [[], [1], [9], [1, 9]]
        )
    ],
)
def test_task2_affordable_subsequences_custom(
    budget: int, ints: list[int], expected: list[list[int]]
) -> None:
    actual = task2.affordable_subsequences(budget, ints)
    assert_equal_task2(actual, expected)

## TASK 3
def assert_equal_task3(
    dict1: dict[str, list[int]], dict2: dict[str, list[int]]
) -> None:
    assert dict1.keys() == dict2.keys()
    for key in dict1:
        dict1[key].sort()
    for key in dict2:
        dict2[key].sort()
    assert dict1 == dict2

d1 = {"id": 1, "favorite_num": 1, "scoops_of_ice_cream": 1}
d2 = {"id": 2, "favorite_num": 142, "scoops_of_ice_cream": 3}
d3 = {"id": 3, "scoops_of_ice_cream": 3}
d4 = {"id": 4, "favorite_num": 142, "year": 2026}

d5 = {"id": 10, "score": 95}
d6 = {"id": 20, "score": 88}
d7 = {"id": 10, "score": 88}

def test_task3_empty() -> None:
    assert_equal_task3(task3.merge_dictionaries([]), {})

def test_task3_full_merge() -> None:
    """Tests the full merge of d1, d2, d3, d4."""
    actual = task3.merge_dictionaries([d1, d2, d3, d4])
    expected = {
        "id": [1, 2, 3, 4],
        "favorite_num": [1, 142],
        "scoops_of_ice_cream": [1, 3],
        "year": [2026],
    }
    assert_equal_task3(actual, expected)

## TASK 4
def test_task4_no_overlapping_features() -> None:
    """
    Write a test that creates two cards with no overlapping feature names.
    Check that conflicting_features returns the correct value (which is
    the empty dictionary).
    """
    c1 = Card({"color": "red", "shape":"circle"})
    c2 = Card({"number": "4", "touch": "smooth"})
    assert c1.conflicting_features(c2.features) == {}


def test_task4_no_conflicting_features() -> None:
    """
    Write a test that creates two cards with one common feature and
    no conflicting features. Check that conflicting_features returns
    the correct value (which is the empty dictionary).
    """
    c1 = Card({"color": "red", "shape":"circle"})
    c2 = Card({"color": "red", "size": "big"})
    assert c1.conflicting_features(c2.features) == {}


def test_task4_one_conflicting_feature() -> None:
    """
    Write a test that creates two cards with two common feature names,
    called "shape" and "number". The two cards should have the same value,
    "square", for "shape". That is, {"shape": "square"} is a common feature.
    For "number", the two cards should have different values, "1" and "7".
    Check that conflicting_features returns a dictionary that maps "number"
    to a pair with "1" and "7".
    """
    c1 = Card({"shape": "square", "number": "1"})
    c2 = Card({"shape": "square", "number": "7"})
    assert c1.conflicting_features(c2.features) == {"number": ("1","7")}


def test_task4_two_conflicting_features() -> None:
    """
    Write a test that creates two cards with three conflicting features,
    and check that conflicting_features returns the correct value.
    """
    c1 = Card({"shape": "square", "number": "1", "color": "red"})
    c2 = Card({"shape": "rectangle", "number": "2", "color": "blue"})
    assert c1.conflicting_features(c2.features) == {"shape": ("square", \
        "rectangle"), "number": ("1","2"), "color": ("red", "blue")}