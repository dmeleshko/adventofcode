import typing
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    val: str = '.'


def dist(p1: Point, p2: Point) -> int:
    return abs(p1.x-p2.x)+abs(p1.y-p2.y)


abc = 'abcdefghijklmnopqrstuvwxyz'


def calc_grid_params(points):
    min_x, max_x, min_y, max_y = 1000, 0, 1000, 0
    for point in points:
        if point.x < min_x:
            min_x = point.x
        if point.x > max_x:
            max_x = point.x
        if point.y < min_y:
            min_y = point.y
        if point.y > max_y:
            max_y = point.y
    return min_x, max_x, min_y, max_y


def translate_points(points, min_x, min_y):
    return [
        Point(p.x-min_x, p.y-min_y, p.val)
        for p in points
    ]


def calc_closest_point(p: Point, points: typing.List[Point]):
    distances = [
        (point, dist(p, point))
        for point in points
    ]
    sorted_dists = sorted(distances, key=lambda x: x[1])
    if sorted_dists[0][1] == sorted_dists[1][1]:
        return None
    else:
        return sorted_dists[0][0]


def calc_areas(grid, skip_points):
    areas = {}
    for row in grid:
        for p in row:
            if p is None or p.val in skip_points:
                continue
            if p.val not in areas:
                areas[p.val] = 0
            areas[p.val] += 1
    return areas.values()


def part1(points: typing.List[Point]) -> int:
    min_x, max_x, min_y, max_y = calc_grid_params(points)
    rows = max_y - min_y + 1
    cols = max_x - min_x + 1
    translated_points = translate_points(points, min_x, min_y)
    grid = [[None]*cols for _ in range(rows)] # type: typing.List[typing.List[typing.Union[None, Point]]]
    for p in translated_points:
        grid[p.y][p.x] = p
    for x in range(cols):
        for y in range(rows):
            if grid[y][x] is None:
                grid[y][x] = calc_closest_point(Point(x, y), translated_points)
    infinite_points = set()
    for x in range(cols):
        if grid[0][x] is not None:
            infinite_points.add(grid[0][x].val)
        if grid[-1][x] is not None:
            infinite_points.add(grid[-1][x].val)
    for y in range(rows):
        if grid[y][0] is not None:
            infinite_points.add(grid[y][0].val)
        if grid[y][-1] is not None:
            infinite_points.add(grid[y][-1].val)
    areas = calc_areas(grid, infinite_points)
    return max(areas)


def calc_total_distances(points, rows, cols):
    return [
        sum([
            dist(Point(x,y), p)
            for p in points
        ])
        for x in range(cols)
        for y in range(rows)
    ]


def part2(points: typing.List[Point]) -> int:
    min_x, max_x, min_y, max_y = calc_grid_params(points)
    rows = max_y - min_y + 1
    cols = max_x - min_x + 1
    translated_points = translate_points(points, min_x, min_y)
    total_distances = calc_total_distances(translated_points, rows, cols)
    return len(list(filter(lambda d: d<10000, total_distances)))


def parse_input(lines: typing.List[str]):
    return [
        Point(*(map(int, coords.strip().split(', '))), i)
        for i, coords in enumerate(lines)
    ]


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(part2(parse_input(fp.readlines())))
