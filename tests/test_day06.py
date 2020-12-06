import pytest
from day06 import part_one, part_two

test_input1 = """abcx
abcy
abcz
"""

test_input2 = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.mark.parametrize('puzzle_input, expected', [
    (test_input1, 6),
    (test_input2, 11),
])
def test_part_one(puzzle_input, expected):
    assert expected == sum(part_one(puzzle_input))


def test_part_two():
    assert 6 == sum(part_two(test_input2))
