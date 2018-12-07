import typing
from itertools import chain


def get_available_steps(
        steps: typing.Dict[str, typing.Set[str]],
        ignore_steps: typing.Set[str] = None
) -> typing.List[str]:
    if ignore_steps is None:
        ignore_steps = set()

    available_steps = set(
        item[0]
        for item in steps.items()
        if len(item[1]) == 0
    )

    dependencies = set(chain.from_iterable(steps.values()))
    keys = set(steps.keys())
    available_steps = available_steps.union(dependencies - keys)
    return sorted(available_steps - ignore_steps)


def get_next_step(steps: typing.Dict[str, typing.Set[str]]) -> str:
    available_steps = get_available_steps(steps)
    return available_steps[0]


def make_step(steps, step) -> typing.Dict[str, typing.Set[str]]:
    if step in steps:
        steps.pop(step)
    for k, v in steps.items():
        steps[k] -= {step}
    return steps


def part1(data: typing.Dict[str, typing.Set[str]]) -> str:
    steps = data
    result = []
    while len(steps) > 0:
        next_step = get_next_step(steps)
        result.append(next_step)
        steps = make_step(steps, next_step)
    return ''.join(result)


def char_to_seconds(char: str):
    return ord(char) - 5


def part2(steps: typing.Dict[str, typing.Set[str]], workers_count: int) -> int:
    result = []
    second = 0
    workers_steps = ['.']*workers_count
    workers_times = [0]*workers_count
    while len(steps) > 0:
        current_steps = set(workers_steps) - {'.'}
        next_steps = get_available_steps(steps, current_steps)
        # get new steps
        for worker, step in enumerate(workers_steps):
            if step == '.' and next_steps:
                next_step = next_steps.pop(0)
                workers_steps[worker] = next_step
                workers_times[worker] = char_to_seconds(next_step)
            elif step != '.':
                workers_times[worker] -= 1
        # finish steps
        for worker, time in enumerate(workers_times):
            if time == 0 and workers_steps[worker] != '.':
                result.append(workers_steps[worker])
                steps = make_step(steps, workers_steps[worker])
                workers_steps[worker] = '.'
        second += 1
    return second


def parse_input(lines: typing.List[str]) -> typing.Dict[str, typing.Set[str]]:
    steps: typing.Dict[str, typing.Set[str]] = dict()
    for line in lines:
        _, dependency, _, _, _, _, _, step, _, _ = line.split()
        if step not in steps:
            steps[step] = {dependency}
        else:
            steps[step].add(dependency)
    return steps


if __name__ == '__main__':
    with open('input.txt') as fp:
        lines = fp.readlines()
    data = parse_input(lines)
    print(part2(data, 5))
