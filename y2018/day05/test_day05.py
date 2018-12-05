from y2018.day05.day05 import part1, part2


def test_part1():
    assert part1(list('aA')) == 0
    assert part1(list('abBA')) == 0
    assert part1(list('abAB')) == 4
    assert part1(list('aabAAB')) == 6
    assert part1(list('dabAcCaCBAcCcaDA')) == 10


def test_part2():
    assert part2('dabAcCaCBAcCcaDA') == 4
