import typing


def cmp_helper(ch1: str, ch2: str):
    return not (
        ch1.islower() and ch2 == ch1.upper()
        or
        ch1.isupper() and ch2 == ch1.lower()
    )


def part1(s: typing.List[str]) -> int:
    result = None
    removals = None
    while removals != 0:
        removals = 0
        i = 0
        if result is not None:
            source = result
        else:
            source = s
        n = len(source)
        result = []
        while True:
            if i == n-1:
                result.append(source[i])
            if i >= n-1:
                break
            if cmp_helper(source[i], source[i+1]):
                result.append(source[i])
                i += 1
            else:
                removals += 1
                i += 2
    return len(result)


def part2(s: str) -> int:
    results = []
    char_set = set(s.lower())
    for i, ch_to_remove in enumerate(char_set):
        s1 = s.replace(ch_to_remove, '')
        s1 = s1.replace(ch_to_remove.upper(), '')
        results.append(part1(list(s1)))
    return min(results)


if __name__ == '__main__':
    with open('input.txt') as fp:
        line = fp.read()

    print(part2(line[:-1]))
