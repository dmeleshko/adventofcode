import re
from collections import Counter
from itertools import chain


def parse_line(s: str):
    return re.findall(r'\[(\d\d\d\d-\d\d-\d\d \d\d:\d\d)\]\s(.*)', s)[0]


def parse_command(command: str):
    if command.startswith('Guard'):
        return 'guard', int(command.split(' ')[1][1:])
    elif command.startswith('wakes'):
        return 'up', None
    else:
        return 'down', None


def calc_sleep_minutes(sleep_start: str, sleep_end: str):
    search_result1 = re.findall(r'.*-(\d\d)-(\d\d) (\d\d):(\d\d)', sleep_start)[0]
    search_result2 = re.findall(r'.*-(\d\d)-(\d\d) (\d\d):(\d\d)', sleep_end)[0]
    month, day, _, start_minute = map(int, search_result1)
    _, _, _, end_minute = map(int, search_result2)
    return f"{month}-{day}", list(range(start_minute, end_minute))


def part1():
    guard_logs = get_guard_logs()
    guard_sleeps_length = [
        (guard, len(list(chain.from_iterable(logs.values()))))
        for guard, logs in guard_logs.items()
    ]
    max_sleep_guard = sorted(guard_sleeps_length, key=lambda k: k[1])[-1][0]
    max_sleep_minute = Counter(
        chain.from_iterable(guard_logs[max_sleep_guard].values())
    ).most_common()[0][0]
    return max_sleep_guard*max_sleep_minute


def get_most_common_minute(guard, logs):
    most_common = Counter(chain.from_iterable(logs.values())).most_common()[0]
    return guard, most_common[0], most_common[1]


def part2():
    guard_logs = get_guard_logs()
    most_common_minutes = [
        get_most_common_minute(guard, logs)
        for guard, logs in guard_logs.items()
        if len(logs) > 0
    ]
    max_minute = sorted(most_common_minutes, key = lambda m: m[2])[-1]
    return max_minute[0]*max_minute[1]


def get_guard_logs():
    with open('input.txt') as fp:
        lines = fp.readlines()
    parsed = map(parse_line, lines)
    sorted_logs = sorted(parsed, key=lambda x: x[0])
    guard_logs = {}
    current_guard = None
    sleep_start = None
    for ts, command in sorted_logs:
        cmd, guard = parse_command(command)
        if cmd == 'guard':
            if guard not in guard_logs:
                guard_logs[guard] = {}
            current_guard = guard
        elif cmd == 'down':
            sleep_start = ts
        elif cmd == 'up':
            sleep_end = ts
            date, minutes = calc_sleep_minutes(sleep_start, sleep_end)
            if date not in guard_logs[current_guard]:
                guard_logs[current_guard][date] = []
            guard_logs[current_guard][date].extend(minutes)
    return guard_logs


if __name__ == '__main__':
    print(part2())
