from typing import List, Tuple


test_input = """F10
N3
F7
R90
F11
"""


def turn(current_direction: str, turn_direction: str, degrees: int) -> str:
    distance_keys = ['N', 'E', 'S', 'W']
    current_index = distance_keys.index(current_direction)

    if turn_direction == 'L':
        degrees = -degrees
    new_direction = distance_keys[(int(degrees/90) + current_index) % 4]
    # else:
    #     new_direction = distance_keys[(int(-degrees/90) + current_index) % 4]

    return new_direction


def part_one(puzzle_input: List[Tuple[str, int]]) -> int:
    x, y = 0, 0

    current_direction = 'E'
    distances = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0,
    }

    for instruction in puzzle_input:
        # print(f'Current Direction: {current_direction}')
        action, distance = instruction
        if action in ('R', 'L'):
            current_direction = turn(current_direction, action, distance)
            continue
        elif action == 'F':
            action = current_direction

        # if action == 'E':
        #     x += distance
        # elif action == 'W':
        #     x -= distance
        # elif action == 'N':
        #     y += distance
        # elif action == 'S':
        #     y -= distance

        distances[action] += distance

    return abs(distances['N'] - distances['S']) + abs(distances['E'] - distances['W'])




if __name__ == '__main__':
    with open('day12_input.txt', 'r') as f:
        puzzle_input = [(line[0], int(line[1:])) for line in f.read().strip().split()]

    # puzzle_input = [(line[0], int(line[1:])) for line in test_input.strip().split()]

    print(f'Part 1: {part_one(puzzle_input)}')

