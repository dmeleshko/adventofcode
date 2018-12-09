import typing
from dataclasses import dataclass


def part1(data: typing.Iterable[int]) -> int:
    current_children_cnt = []
    current_metadata_cnt = []
    sum = 0
    for n in data:
        if len(current_children_cnt) == 0:
            current_children_cnt.append(n)
        elif len(current_children_cnt) > len(current_metadata_cnt):
            current_metadata_cnt.append(n)
        elif current_children_cnt[-1] > 0:
            current_children_cnt[-1] -= 1
            current_children_cnt.append(n)
        elif current_children_cnt[-1] == 0 and current_metadata_cnt[-1] > 0:
            current_metadata_cnt[-1] -= 1
            sum += n
        if current_children_cnt[-1] == 0 and current_metadata_cnt[-1] == 0:
            current_children_cnt.pop()
            current_metadata_cnt.pop()
    return sum


@dataclass
class Node:
    prev_node: typing.Optional
    nodes: typing.List
    metadata: typing.List[int]


def calc_value(n: Node):
    nodes_count = len(n.nodes)
    if nodes_count == 0:
        return sum(n.metadata)
    result = 0
    for i in n.metadata:
        if (i-1) < nodes_count:
            result += calc_value(n.nodes[i-1])
    return result


def part2(data: typing.Iterable[int]) -> int:
    current_node = Node(None, [], [])
    root = current_node
    current_children_cnt = []
    current_metadata_cnt = []
    for n in data:
        if len(current_children_cnt) == 0:
            current_children_cnt.append(n)
        elif len(current_children_cnt) > len(current_metadata_cnt):
            current_metadata_cnt.append(n)
        elif current_children_cnt[-1] > 0:
            current_children_cnt[-1] -= 1
            current_children_cnt.append(n)
            current_node = Node(current_node, [], [])
            current_node.prev_node.nodes.append(current_node)
        elif current_children_cnt[-1] == 0 and current_metadata_cnt[-1] > 0:
            current_metadata_cnt[-1] -= 1
            current_node.metadata.append(n)
        if current_children_cnt[-1] == 0 and current_metadata_cnt[-1] == 0:
            current_children_cnt.pop()
            current_metadata_cnt.pop()
            current_node = current_node.prev_node
    return calc_value(root)


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(part2(map(int, fp.readline().strip().split())))
