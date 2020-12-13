from typing import Dict, List, Tuple


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

        distances[action] += distance

    return abs(distances['N'] - distances['S']) + abs(distances['E'] - distances['W'])


def rotate_waypoints(waypoints: Dict[str, int], direction: int, degrees: int) -> None:
    positions = ['E', 'S', 'W', 'N']
    # positions += positions.copy() + positions.copy() + positions.copy()
    rotation_length = int(degrees/90)
    extra = 1

    for _ in range(rotation_length):
        temp_value = waypoints['E']

        if direction == 'R':
            range_iterator = range(4)
        else:
            extra = -1
            range_iterator = range(0, -4, -1)

        for i in range_iterator:
            temp_value, waypoints[positions[(i + extra) % 4]] = waypoints[positions[(i + extra) % 4]], temp_value


def part_two(puzzle_input):
    # current_direction = 'E'

    ship_distances = {
        'E': 0,
        'W': 0,
        'N': 0,
        'S': 0,
    }

    waypoint_distances = {
        'E': 10,
        'W': 0,
        'N': 1,
        'S': 0,
    }

    for instruction in puzzle_input:
        action, distance = instruction
        if action in ('R', 'L'):
            rotate_waypoints(waypoint_distances, action, distance)
            continue
        elif action == 'F':
            for ship_direction in ship_distances.keys():
                ship_distances[ship_direction] += waypoint_distances[ship_direction] * distance
        else:
            waypoint_distances[action] += distance

        # print(f'ship_distances: {ship_distances}')
        # print(f'waypoint_distances: {waypoint_distances}')

    return abs(ship_distances['N'] - ship_distances['S']) + abs(ship_distances['E'] - ship_distances['W'])


if __name__ == '__main__':
    with open('day12_input.txt', 'r') as f:
        puzzle_input = [(line[0], int(line[1:])) for line in f.read().strip().split()]

    print(f'Part 1: {part_one(puzzle_input)}')
    print(f'Part 2: {part_two(puzzle_input)}')
