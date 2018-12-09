import typing
from dataclasses import dataclass


@dataclass
class LinkedList:
    prev_elem: typing.Optional = None
    next_elem: typing.Optional = None
    value: int = 0


def part1(players_count: int, max_score: int) -> int:
    marble_value = 0
    scores = [0]*players_count

    first_item = LinkedList(None, None, marble_value)
    current_item = first_item
    current_item.next_elem = current_item
    current_item.prev_elem = current_item

    current_player = 0
    real_max_score = 23 * (max_score // 23)
    while marble_value <= real_max_score:
        marble_value += 1
        if marble_value % 23 == 0:
            current_item = current_item.prev_elem.prev_elem.prev_elem.prev_elem.prev_elem.prev_elem.prev_elem
            scores[current_player] += marble_value + current_item.value
            current_item.prev_elem.next_elem = current_item.next_elem
            current_item.next_elem.prev_elem = current_item.prev_elem
            current_item = current_item.next_elem
        else:
            current_item = current_item.next_elem.next_elem
            new_item = LinkedList(current_item.prev_elem, current_item, marble_value)
            current_item.prev_elem.next_elem = new_item
            current_item.prev_elem = new_item
            current_item = new_item
        current_player = (current_player + 1) % players_count
    return max(scores)


def part2(players_count: int, max_score: int) -> int:
    return part1(players_count, max_score*100)


if __name__ == '__main__':
    print(part2(476, 71431))
