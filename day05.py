from typing import Set


def get_seat_row(seat_code: str) -> int:
    seat_rows = list(range(128))
    last_letter = None

    for i, letter in enumerate(seat_code[:7]):
        if letter == 'F':
            seat_rows = seat_rows[:len(seat_rows) // 2]
        else:
            seat_rows = seat_rows[len(seat_rows) // 2:]

        last_letter = letter
        # print(f'{min(seat_rows)} - {max(seat_rows)}')

    return min(seat_rows) if last_letter == 'F' else max(seat_rows)


def get_seat_number(seat_code: str) -> int:
    seat_colums = list(range(8))
    last_letter = None

    for i, letter in enumerate(seat_code[-3:]):
        if letter == 'L':
            seat_colums = seat_colums[:len(seat_colums) // 2]
        else:
            seat_colums = seat_colums[len(seat_colums) // 2:]

        last_letter = letter
        # print(f'{min(seat_colums)} - {max(seat_colums)}')

    return min(seat_colums) if last_letter == 'L' else max(seat_colums)


def get_boarded_seats(puzzle_input: str) -> Set[int]:
    seat_ids = set()
    for seat_code in puzzle_input.split():
        row = get_seat_row(seat_code)
        seat = get_seat_number(seat_code)

        seat_ids.add(row * 8 + seat)

    return seat_ids


def part_one(puzzle_input: str) -> int:
    return max(get_boarded_seats(puzzle_input))


def part_two(puzzle_input: str) -> int:
    sorted_seats = sorted(get_boarded_seats(puzzle_input))
    for i, seat_id in enumerate(sorted_seats):
        if seat_id + 2 == sorted_seats[i + 1] and seat_id + 1 != sorted_seats[i + 1]:
            return seat_id + 1


if __name__ == '__main__':
    with open('day05_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Part 1 - Highest Seat ID: {part_one(puzzle_input)}')
    print(f'Part 2 - My Seat ID: {part_two(puzzle_input)}')
