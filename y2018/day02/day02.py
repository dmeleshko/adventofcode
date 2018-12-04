import typing
from collections import Counter
from functools import reduce


def classify(s: str) -> typing.Tuple[int, int]:
    counter = Counter(s)
    if counter.most_common()[0][1] == 3 and counter.most_common()[1][1] == 2:
        return 1, 1
    elif counter.most_common()[0][1] == 3:
        return 1, 0
    elif counter.most_common()[0][1] == 2:
        return 0, 1
    return 0, 0


def part1(inp: typing.List[str]) -> int:
    step1 = map(classify, inp)
    step2 = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), step1, (0, 0))
    step3 = step2[0]*step2[1]
    return step3


def calc_diff(s1: str, s2: str) -> str:
    step1 = zip(s1, s2)
    step2 = filter(lambda x: x[0] == x[1], step1)
    step3 = ''.join(map(lambda x: x[0], step2))
    return step3


def part2(inp: typing.List[str]) -> str:
    count = len(inp)
    lenght = len(inp[0])
    for i in range(count-1):
        for j in range(i+1, count):
            diff = calc_diff(inp[i], inp[j])
            if lenght-len(diff) == 1:
                return diff
    return ''


def parse_input() -> typing.List[str]:
    with open('input.txt') as fp:
        lines = fp.readlines()
    return lines


if __name__=='__main__':
    inp = parse_input()
    print(part2(inp))
