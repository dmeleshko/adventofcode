from y2018.day09.day09 import part1, part2


def test_part1():
    assert part1(9, 25) == 32
    assert part1(9, 50) == 63
    assert part1(9, 200) == 227
    assert part1(10, 1618) == 8317
    assert part1(13, 7999) == 146373
    assert part1(17, 1104) == 2764
    assert part1(21, 6111) == 54718
    assert part1(30, 5807) == 37305
    assert part1(476, 71431) == 384205


def test_part2():
    assert part2(476, 71431) == 3066307353
