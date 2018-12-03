import pytest

from y2018.day03 import day03


def test_parse_string(
        input1, input2, input3,
        claim1, claim2, claim3,
):
    assert day03.parse_string(input1) == claim1
    assert day03.parse_string(input2) == claim2
    assert day03.parse_string(input3) == claim3


def test_parse_input(inputs, claims):
    assert day03.parse_input(inputs) == claims


def test_part1(claims):
    assert day03.part1(claims) == 4


def test_part2(claims):
    assert day03.part2(claims) == 3


def test_make_grid(grid, claims):
    day03.MAX_GRID = 8
    assert (
        day03.make_grid(claims) == grid
    )


def test_get_claim(grid, claim1, claim2, claim3):
    assert list(day03.get_claim(grid, claim1)) == [
        [1, 1,-1,-1], [1, 1,-1,-1], [1, 1, 1, 1], [1, 1, 1, 1]
    ]
    assert list(day03.get_claim(grid, claim2)) == [
        [2, 2, 2, 2], [2, 2, 2, 2], [-1,-1, 2, 2], [-1,-1, 2, 2]
    ]
    assert list(day03.get_claim(grid, claim3)) == [[3, 3], [3, 3]]
