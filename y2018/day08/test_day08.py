import pytest

from y2018.day08.day08 import part1, part2


def test_part1(input_data):
    assert part1(input_data) == 138


def test_part2(input_data):
    assert part2(input_data) == 66


@pytest.fixture()
def input_data():
    return map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.strip().split())
