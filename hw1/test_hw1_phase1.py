"""
CMSC 14200, Spring 2026
Homework 1, Phase 1 Tests
"""

import pytest

import task1
import task2
import task3


## TASK 1


def test_task1_to_base_2_0() -> None:
    assert task1.to_base_n(2, 0) == "0_2_0"


def test_task1_to_base_2_7() -> None:
    assert task1.to_base_n(2, 7) == "0_2_111"


def test_task1_to_base_2_8() -> None:
    assert task1.to_base_n(2, 8) == "0_2_1000"


def test_task1_to_base_2_142() -> None:
    assert task1.to_base_n(2, 142) == "0_2_10001110"


# NOTE: Compared to the individual tests for to_base_n(2, ...) above,
# the following definition includes multiple tests for to_base_n(9, ...)
# in a single "parameterized" test. Don't worry about how this pytest
# library function is working. Just know that you can add more tests by
# adding to the lists that appear in @pytest.mark.parametrize annotations
# before each test.


@pytest.mark.parametrize(
    "n, expected", [(0, "0_9_0"), (81, "0_9_100"), (80, "0_9_88")]
)
def test_task1_to_base_9(n: int, expected: str) -> None:
    assert task1.to_base_n(9, n) == expected


def test_task1_from_base_2_111() -> None:
    assert task1.from_base_n("0_2_111") == 7


def test_task1_from_base_9_88() -> None:
    assert task1.from_base_n("0_9_88") == 80


@pytest.mark.parametrize("s, expected", [("0_9_088", 80), ("0_9_00088", 80)])
def test_task1_leading_zeroes(s: str, expected: int) -> None:
    assert task1.from_base_n(s) == expected


## TASK 2


def assert_equal_task2(list1: list[list[int]], list2: list[list[int]]) -> None:
    # Sort both lists to make comparison easier
    list1.sort()
    list2.sort()
    assert list1 == list2


_1234 = list(range(1, 4))


@pytest.mark.parametrize(
    "budget, ints, expected",
    [
        (0, _1234, [[]]),
        (4, _1234, [[], [1], [2], [1, 2], [3], [1, 3]]),
        (
            6,
            _1234,
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        ),
        (
            6,
            _1234,
            [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []],
        ),
    ],
)
def test_task2_affordable_subsequences_1234(
    budget: int, ints: list[int], expected: list[list[int]]
) -> None:
    assert_equal_task2(task2.affordable_subsequences(budget, ints), expected)


## TASK 3


def assert_equal_task3(
    dict1: dict[str, list[int]], dict2: dict[str, list[int]]
) -> None:
    # Sort to make comparison easier
    for key in dict1:
        dict1[key].sort()
    for key in dict2:
        dict2[key].sort()
    assert dict1 == dict2


d1 = {"id": 1, "favorite_num": 1, "scoops_of_ice_cream": 1}

d2 = {"id": 2, "favorite_num": 142, "scoops_of_ice_cream": 3}

d3 = {"id": 3, "scoops_of_ice_cream": 3}

d4 = {"id": 4, "favorite_num": 142, "year": 2026}


def test_task3_0() -> None:
    assert_equal_task3(task3.merge_dictionaries([]), {})


def test_task3_1() -> None:
    actual = task3.merge_dictionaries([d1])
    expected = {"id": [1], "favorite_num": [1], "scoops_of_ice_cream": [1]}
    assert_equal_task3(actual, expected)


def test_task3_1234() -> None:
    actual = task3.merge_dictionaries([d1, d2, d3, d4])
    expected = {
        "id": [1, 2, 3, 4],
        "favorite_num": [1, 142],
        "scoops_of_ice_cream": [1, 3],
        "year": [2026],
    }
    assert_equal_task3(actual, expected)


def test_task3_1234_reordered() -> None:
    actual = task3.merge_dictionaries([d1, d2, d3, d4])
    expected = {
        "year": [2026],
        "favorite_num": [142, 1],
        "id": [4, 1, 3, 2],
        "scoops_of_ice_cream": [1, 3],
    }
    assert_equal_task3(actual, expected)
