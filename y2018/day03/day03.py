import math
import re
import typing
from dataclasses import dataclass
from itertools import chain

MAX_GRID = 1000


@dataclass
class Claim():
    number: int
    x: int
    y: int
    width: int
    height: int


def parse_string(s: str) -> Claim:
    parse_results = re.findall(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', s)
    return Claim(*map(int, parse_results[0]))


def parse_input(user_input: typing.List[str]) -> typing.List[Claim]:
    return list(map(parse_string, user_input))


def make_grid(claims: typing.List[Claim]) -> typing.List[typing.List[int]]:
    grid = [[0] * MAX_GRID for i in range(MAX_GRID)]
    for claim in claims:
        for i in range(claim.y, claim.y + claim.height):
            for j in range(claim.x, claim.x + claim.width):
                if grid[i][j] > 0 or grid[i][j] < 0:
                    grid[i][j] = -1
                else:
                    grid[i][j] = claim.number
    return grid


def part1(claims: typing.List[Claim]) -> int:
    grid = make_grid(claims)
    count = len(list(filter(lambda x: x == -1, chain.from_iterable(grid))))
    return count


def get_claim(
        grid: typing.List[typing.List[int]],
        claim: Claim
) -> typing.Iterable[typing.Iterable[int]]:
    return map(
        lambda r: r[claim.x:claim.x+claim.width],
        grid[claim.y:claim.y+claim.height]
    )


def is_claim_overlaps(grid: typing.List[typing.List[int]], claim: Claim):
    return -1 in set(chain.from_iterable(get_claim(grid, claim)))


def part2(claims: typing.List[Claim]) -> typing.Optional[int]:
    grid = make_grid(claims)
    for claim in claims:
        if not is_claim_overlaps(grid, claim):
            return claim.number
    return None


if __name__ == '__main__':
    with open('input.txt') as fp:
        lines = fp.readlines()
        user_input = parse_input(lines)
        print(part2(user_input))
