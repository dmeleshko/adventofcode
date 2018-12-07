import pytest

import y2018.day07.day07 as day07


def test_part1(lines):
    data = day07.parse_input(lines)
    assert day07.part1(data) == 'CABDFE'


def test_part2(lines, char_to_seconds_patched):
    data = day07.parse_input(lines)
    assert day07.part2(data, 2) == 15


@pytest.fixture()
def lines():
    return [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
    ]


@pytest.fixture()
def char_to_seconds_patched(monkeypatch):
    def char_to_seconds_(char: str) -> int:
        return ord(char) - 65
    monkeypatch.setattr(day07, 'char_to_seconds', char_to_seconds_)
