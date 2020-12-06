from typing import Set


def parse_seat_code(seat_code: str, code_section: slice, range_count: int) -> int:
    groups = list(range(range_count))
    last_letter = None

    for i, letter in enumerate(seat_code[code_section]):
        if letter in ('F', 'L'):
            groups = groups[:len(groups) // 2]
        else:
            groups = groups[len(groups) // 2:]

        last_letter = letter
        # print(f'{min(groups)} - {max(groups)}')

    return min(groups) if last_letter in ('F', 'L') else max(groups)


def get_seat_row(seat_code: str) -> int:
    return parse_seat_code(seat_code, slice(7), 128)


def get_seat_number(seat_code: str) -> int:
    return parse_seat_code(seat_code, slice(-3, None), 8)


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
