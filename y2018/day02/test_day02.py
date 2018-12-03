from .day02 import part1, part2


def test_part01():
    inp = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab',
    ]
    assert 12 == part1(inp)


def test_part02():
    inp = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ]
    assert 'fgij' == part2(inp)
