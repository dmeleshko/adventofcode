import pytest

from y2018.day06.day06 import Point, part1, parse_input, part2


def test_part1(example_input):
    assert part1(example_input) == 17


def test_part2(example_input):
    assert part2(example_input) == 16


@pytest.fixture()
def example_input():
    inp = [
        '1, 1',
        '1, 6',
        '8, 3',
        '3, 4',
        '5, 5',
        '8, 9',
    ]
    return parse_input(inp)
