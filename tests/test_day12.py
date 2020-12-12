import os
import pytest

from day12 import turn, part_one


test_input = """F10
N3
F7
R90
F11
"""

path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file.replace('tests/', ''))[0]
path_to_file = os.path.join(current_directory, "day12_input.txt")
with open(path_to_file, 'r') as f:
    real_input = f.read().strip()


@pytest.mark.parametrize('current_direction, turn_direction, degrees, expected', [
    ('E', 'R', 90, 'S'),
    ('E', 'L', 180, 'W'),
    ('N', 'R', 270, 'W'),
    ('N', 'R', 360, 'N'),
    ('N', 'L', 279, 'E'),
])
def test_turn(current_direction: str, turn_direction: str, degrees: int, expected: str):
    new_direction = turn(current_direction, turn_direction, degrees)

    assert expected == new_direction


@pytest.mark.parametrize('puzzle_input, expected', [
    (test_input, 25),
    (real_input, 420),
])
def test_part_one(puzzle_input: str, expected: int):
    instructions = [(line[0], int(line[1:])) for line in puzzle_input.split()]

    assert expected == part_one(instructions)
