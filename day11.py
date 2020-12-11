

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


def get_line_of_sight_count(seats, current_row: int, current_column: int) -> int:
    row_max = len(seats) - 1
    col_max = len(seats[0]) - 1

    occupied_count = 0

    adjacent_coordinates = []

    if current_row != 0:
        # up
        up_found = False
        up_left_found = False
        up_right_found = False
        last_col_l = last_col_r = current_column
        for row in range(current_row - 1, -1, -1):
            # if row > row_max or row == current_row:
            #     continue
            if seats[row][current_column] in ('#', 'L') and not up_found:
                if seats[row][current_column] == '#':
                    occupied_count += 1
                up_found = True
                adjacent_coordinates.append((row, current_column))

            # up left
            if last_col_l != 0:
                last_col_l -= 1
                if seats[row][last_col_l] in ('#', 'L') and not up_left_found:
                    if seats[row][last_col_l] == '#':
                        occupied_count += 1
                    up_left_found = True
                    adjacent_coordinates.append((row, last_col_l))

            # up right
            if last_col_r < col_max:
                last_col_r += 1
                if seats[row][last_col_r] in ('#', 'L') and not up_right_found:
                    if seats[row][last_col_r] == '#':
                        occupied_count += 1
                    up_right_found = True
                    adjacent_coordinates.append((row, last_col_r))

    # down
    last_col_l = last_col_r = current_column
    down_found = False
    down_left_found = False
    down_right_found = False
    if current_row < row_max:
        for row in range(current_row + 1, row_max + 1):
            if seats[row][current_column] in ('#', 'L') and not down_found:
                if seats[row][current_column] == '#':
                    occupied_count += 1
                down_found = True
                adjacent_coordinates.append((row, current_column))

            # down left
            if last_col_l != 0:
                last_col_l -= 1
                if seats[row][last_col_l] in ('#', 'L') and not down_left_found:
                    if seats[row][last_col_l] == '#':
                        occupied_count += 1
                    down_left_found = True
                    adjacent_coordinates.append((row, last_col_l))

            # down right
            if last_col_r < col_max:
                last_col_r += 1
                if seats[row][last_col_r] in ('#', 'L') and not down_right_found:
                    if seats[row][last_col_r] == '#':
                        occupied_count += 1
                    down_right_found = True
                    adjacent_coordinates.append((row, last_col_r))

    # left
    left_found = False
    if current_column != 0:
        for col in range(current_column - 1, -1, -1):
            # if col > col_max or col == current_column:
            #     continue
            if seats[current_row][col] in ('#', 'L') and not left_found:
                if seats[current_row][col] == '#':
                    occupied_count += 1
                left_found = True
                adjacent_coordinates.append((current_row, col))
                break

    # right
    right_found = False
    if current_column < col_max:
        for col in range(current_column + 1, col_max + 1):
            if seats[current_row][col] in ('#', 'L') and not right_found:
                if seats[current_row][col]  == '#':
                    occupied_count += 1
                right_found = True
                adjacent_coordinates.append((current_row, col))
                break

    return occupied_count


def count_occupied_adjacents(seats, adjacent_coordinates) -> int:
    occupied_count = 0
    for row, col in adjacent_coordinates:
        if seats[row][col] == '#':
            occupied_count += 1

    return occupied_count


def adjacents_empty(seats, adjacent_coordinates) -> bool:
    for row, col in adjacent_coordinates:
        if seats[row][col] == '#':
            return False
    return True


def print_seats(seats):
    for row in seats:
        print(''.join(row))


def part_one(seats):
    # done = False
    occupied_seats = 0
    while True:
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
            # done = True
            return occupied_seats


def part_two(seats) -> int:
    occupied_seats = 0
    while True:
        changed_seats = False
        temp_seats = deepcopy(seats)
        for i, row in enumerate(temp_seats):
            for j, column in enumerate(row):
                if column == '.':
                    continue
                adjacent_occupied_count = get_line_of_sight_count(temp_seats, i, j)
                if adjacent_occupied_count == 0 and column == 'L':
                    seats[i][j] = '#'
                    changed_seats = True
                    occupied_seats += 1
                elif adjacent_occupied_count >= 5 and column == '#':
                    seats[i][j] = 'L'
                    changed_seats = True
                    if occupied_seats > 0:
                        occupied_seats -= 1

        # print_seats(seats)
        # print('\n\n')
        if not changed_seats:
            # done = True
            return occupied_seats


if __name__ == '__main__':
    with open('day11_input.txt', 'r') as f:
        puzzle_input = f.read().strip().split()

    # puzzle_input = test_input.strip().split()

    seats = [list(line) for line in puzzle_input]

    print(f'Part 1: {part_one(deepcopy(seats))}')
    print(f'Part 2: {part_two(deepcopy(seats))}')
