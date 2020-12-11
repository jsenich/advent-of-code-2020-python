

from typing import List, Tuple
from copy import deepcopy


test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def get_adjacent_coordinates(seats, current_row: int, current_column: int) -> List[Tuple[int, int]]:
    row_max = len(seats) - 1
    col_max = len(seats[0]) - 1

    adjacent_coordinates = []
    if current_row != 0:
        # up
        adjacent_coordinates.append((current_row - 1, current_column))
        if current_column != 0:
            # up-left
            adjacent_coordinates.append((current_row - 1, current_column - 1))
        if current_column < col_max:
            # up-right
            adjacent_coordinates.append((current_row - 1, current_column + 1))
    if current_row < row_max:
        # down
        adjacent_coordinates.append((current_row + 1, current_column))
        if current_column != 0:
            # down-left
            adjacent_coordinates.append((current_row + 1, current_column - 1))
        if current_column < col_max:
            # down-right
            adjacent_coordinates.append((current_row + 1, current_column + 1))
    if current_column != 0:
        # left
        adjacent_coordinates.append((current_row, current_column - 1))
    if current_column < col_max:
        # right
        adjacent_coordinates.append((current_row, current_column + 1))

    return adjacent_coordinates


def adjacents_empty(seats, adjacent_coordinates) -> bool:
    for row, col in adjacent_coordinates:
        if seats[row][col] == '#':
            return False

    return True


def count_occupied_adjacents(seats, adjacent_coordinates) -> int:
    occupied_count = 0
    for row, col in adjacent_coordinates:
        if seats[row][col] == '#':
            occupied_count += 1

    return occupied_count


def print_seats(seats):
    for row in seats:
        print(''.join(row))


if __name__ == '__main__':
    with open('day11_input.txt', 'r') as f:
        puzzle_input = f.read().strip().split()

    seats = [list(line) for line in puzzle_input]

    done = False
    occupied_seats = 0
    while done is False:
        changed_seats = False
        temp_seats = deepcopy(seats)
        for i, row in enumerate(temp_seats):
            for j, column in enumerate(row):
                if column == '.':
                    continue
                adjacent_coords = get_adjacent_coordinates(temp_seats, i, j)
                if adjacents_empty(temp_seats, adjacent_coords) and column == 'L':
                    seats[i][j] = '#'
                    changed_seats = True
                    occupied_seats += 1
                elif count_occupied_adjacents(temp_seats, adjacent_coords) >= 4 and column == '#':
                    seats[i][j] = 'L'
                    changed_seats = True
                    if occupied_seats > 0:
                        occupied_seats -= 1

        # print_seats(seats)
        # print('\n\n')
        if not changed_seats:
            done = True

    print(f'Part 1: {occupied_seats}')
