import os
import pytest

from day12 import part_one, part_two, turn, rotate_waypoints


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


@pytest.mark.parametrize('direction, degrees, expected', [
    ('R', 90, {'E': 4, 'S': 1, 'W': 2, 'N': 3}),
    ('L', 90, {'E': 2, 'S': 3, 'W': 4, 'N': 1}),
    ('R', 180, {'E': 3, 'S': 4, 'W': 1, 'N': 2}),
    ('L', 180, {'E': 3, 'S': 4, 'W': 1, 'N': 2}),
    ('R', 270, {'E': 2, 'S': 3, 'W': 4, 'N': 1}),
    ('L', 270, {'E': 4, 'S': 1, 'W': 2, 'N': 3}),
])
def test_rotate_waypoints(direction, degrees, expected):
    waypoints = {'E': 1, 'S': 2, 'W': 3, 'N': 4}

    rotate_waypoints(waypoints, direction, degrees)
    assert expected == waypoints


@pytest.mark.parametrize('puzzle_input, expected', [
    (test_input, 286),
    (real_input, 42073),
])
def test_part_two(puzzle_input: str, expected: int):
    instructions = [(line[0], int(line[1:])) for line in puzzle_input.split()]

    assert expected == part_two(instructions)
