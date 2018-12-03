import pytest

from y2018.day03 import day03


@pytest.fixture()
def input1():
    return '#1 @ 1,3: 4x4'


@pytest.fixture()
def input2():
    return '#2 @ 3,1: 4x4'


@pytest.fixture()
def input3():
    return '#3 @ 5,5: 2x2'


@pytest.fixture()
def inputs(input1, input2, input3):
    return [input1, input2, input3]


@pytest.fixture()
def claim1():
    return day03.Claim(1, 1, 3, 4, 4)


@pytest.fixture()
def claim2():
    return day03.Claim(2, 3, 1, 4, 4)


@pytest.fixture()
def claim3():
    return day03.Claim(3, 5, 5, 2, 2)


@pytest.fixture()
def claims(claim1, claim2, claim3):
    return [claim1, claim2, claim3]


@pytest.fixture()
def grid():
    return [
        [0] * 8,
        [0, 0, 0, 2, 2, 2, 2, 0],
        [0, 0, 0, 2, 2, 2, 2, 0],
        [0, 1, 1, -1, -1, 2, 2, 0],
        [0, 1, 1, -1, -1, 2, 2, 0],
        [0, 1, 1, 1, 1, 3, 3, 0],
        [0, 1, 1, 1, 1, 3, 3, 0],
        [0] * 8,
    ]


