import typing
from itertools import cycle


def parse_input() -> typing.List[int]:
    with open('input.txt') as fp:
        lines = fp.readlines()
        changes = list(map(int, lines))
    return changes


def part1(changes: typing.List[int]) -> int:
    frequency = sum(changes)
    return frequency


def part2(changes: typing.List[int]) -> int:
    frequency = 0
    frequencies = {0}
    for change in cycle(changes):
        frequency += change
        if frequency in frequencies:
            return frequency
        frequencies.add(frequency)


if __name__ == '__main__':
    print(part2(parse_input()))
