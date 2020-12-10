import os

import pytest

from day08 import part_one, part_two


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file.replace('tests/', ''))[0]
print(current_directory)
path_to_file = os.path.join(current_directory, "day08_input.txt")
with open(path_to_file, 'r') as f:
    real_input = f.read().strip()


@pytest.mark.parametrize('puzzle_input, expected', [
    (test_input, 5),
    (real_input, 1859)
])
def test_part_one(puzzle_input, expected):
    assert expected == part_one(puzzle_input)


@pytest.mark.parametrize('puzzle_input, expected', [
    (test_input, 8),
    (real_input, 1235)
])
def test_part_two(puzzle_input, expected):
    assert expected == part_two(puzzle_input)
