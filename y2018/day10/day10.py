import re
import typing
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    dx: int
    dy: int


def parse_lines(lines: typing.Iterable[str]) -> typing.List[Point]:
    regex = re.compile('.*<\s*([-\d]+),\s*([-\d]+)> .*<\s*([-\d]+),\s*([-\d]+)>')
    points = []
    for line in lines:
        x, y, dx, dy = map(int, regex.findall(line)[0])
        points.append(Point(x, y, dx, dy))
    return points


def calc_max_height(points: typing.Iterable[Point]):
    _, min_y = min_params(points)
    _, max_y = max_params(points)
    return abs(max_y-min_y)


def calc_grid(points: typing.Iterable[Point]) -> typing.Iterable[Point]:
    for point in points:
        point.x += point.dx
        point.y += point.dy
    return points


def calc_prev_grid(points: typing.Iterable[Point]) -> typing.Iterable[Point]:
    for point in points:
        point.x -= point.dx
        point.y -= point.dy
    return points


def min_params(points):
    min_x = min(map(lambda p: p.x, points))
    min_y = min(map(lambda p: p.y, points))
    return min_x, min_y


def translate_points(points):
    min_x, min_y = min_params(points)
    return [
        Point(p.x-min_x, p.y-min_y, 0, 0)
        for p in points
    ]


def max_params(points):
    max_x = max(map(lambda p: p.x, points))
    max_y = max(map(lambda p: p.y, points))
    return max_x, max_y


def print_grid(points):
    max_x, max_y = max_params(points)
    print()
    for y in range(max_y+1):
        for x in range(max_x+1):
            if Point(x, y, 0, 0) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def part1(points: typing.List[Point]):
    prev_height = 999999
    second = 0
    while True:
        max_height = calc_max_height(points)
        if prev_height < max_height:
            break
        prev_height = max_height
        points = calc_grid(points)
        second += 1
    points = translate_points(calc_prev_grid(points))
    print_grid(points)
    print(second-1)
    return second - 1


if __name__ == '__main__':
    with open('input.txt') as fp:
        lines = fp.readlines()
    points = parse_lines(lines)
    part1(points)
