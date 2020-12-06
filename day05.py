
def part_one(puzzle_input: str):
    # test_input = 'FBFBBFFRLR'

    seat_ids = set()
    for seat_input in puzzle_input.split():
        row_start = 0
        row_end = 127
        previous = None
        op = None
        for i, letter in enumerate(seat_input):
            if i == 7:
                break

            result = len(range(row_start, row_end)) // 2
            if letter == 'F':
                op = min
                if previous and previous == 'F':
                    row_end = result
                else:
                    row_end = row_start + result
            elif letter == 'B':
                op = max
                if previous and previous == 'B':
                    row_start += result + 1
                else:
                    row_start = row_end - result

            previous = letter
            print(f'{row_start} - {row_end}')

        final_row = min(row_start, row_end)
        print(f'Row: {final_row}')

        seat_start = 0
        seat_end = 7
        previous = None
        op = None
        for i, letter in enumerate(seat_input[-3:]):
            result = len(range(seat_start, seat_end)) // 2
            if letter == 'L':
                op = min
                if previous and previous == 'L':
                    seat_end = result
                else:
                    seat_end = seat_start + result
            elif letter == 'R':
                op = max
                if previous and previous == 'R':
                    seat_start += result + 1
                else:
                    seat_start = seat_end - result

            previous = letter
            print(f'Seats: {seat_start} - {seat_end}')

        seat = max(seat_start, seat_end)
        print(f'Seat: {seat}')

        seat_id = final_row * 8 + seat
        print(f'Seat ID: {seat_id}')
        seat_ids.add(seat_id)
    return max(seat_ids), seat_ids


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    with open('day05_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    highest_id, filled_seats = part_one(puzzle_input)
    print(f'Highest Seat ID: {highest_id}')
    import pprint
    pprint.pprint(list(chunks(list(filled_seats), 8)))
    # pprint.pprint(list(filled_seats))

    sorted_seats = sorted(list(filled_seats))
    for i, num in enumerate(sorted_seats):

        if num + 2 == sorted_seats[i + 1] and num + 1 != sorted_seats[i + 1]:
            print(f"missing: {num + 2}")
            break

    # all_seats = set([i for i in range(highest_id + 1)])
    # empty_seats = list(all_seats - filled_seats)
    # print(f'empty seats: {empty_seats}')
    # pprint.pprint(list(chunks(empty_seats, 8)))
