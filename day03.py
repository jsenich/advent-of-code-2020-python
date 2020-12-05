import math
from typing import List, Tuple


def get_expanded_map(map_input: str, right_distance: int) -> List[List[str]]:
    map = map_input.split()
    expanded_map = []
    right_distance

    for line in map:
        expanded_map.append(line * math.ceil((len(map) * right_distance)/len(map[0])))

    return expanded_map


def traverse_slope(slope_map: List[List[str]], right: int, down: int) -> int:
    row_pos = 0
    col_pos = 0
    tree_count = 0

    while row_pos <= len(slope_map) - 1:
        if slope_map[row_pos][col_pos] == '#':
            tree_count += 1

        row_pos += down
        col_pos += right

    return tree_count


def part_one(puzzle_input: str, slope: Tuple[int, int]) -> int:
    expanded_map = get_expanded_map(puzzle_input, slope[0])

    return traverse_slope(expanded_map, *slope)


def part_two(puzzle_input: str, slopes: List[Tuple[int, int]]) -> int:
    return math.prod(part_one(puzzle_input, slope) for slope in slopes)

if __name__ == '__main__':
    with open('day03_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Part One Tree Count: {part_one(puzzle_input, (3, 1))}')

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(f'Part Two Tree Counts Product: {part_two(puzzle_input, slopes)}')
