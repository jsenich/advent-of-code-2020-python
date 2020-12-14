import itertools

test_input = """939
7,13,x,x,59,x,31,19
"""


def parse_bus_schedules(departure_time: int, bus_ids: str):
    schedule = {}

    def get_closest(bus_id, departure_time):
        for i in itertools.count(0, bus_id):
            if i >= departure_time:
                return i

    for bus_id in bus_ids.split(','):
        if bus_id == 'x':
            continue
        bus_id = int(bus_id)
        schedule[bus_id] = get_closest(bus_id, departure_time)
    return schedule


def part_one(puzzle_input):
    earliest_time, bus_ids = puzzle_input.split()

    schedule = parse_bus_schedules(int(earliest_time), bus_ids)

    closet_times = list(schedule.values())
    closest_time = min(closet_times)
    bus_ids = list(schedule.keys())
    bus = bus_ids[closet_times.index(closest_time)]

    return bus * (closest_time - int(earliest_time))


if __name__ == '__main__':
    with open('day13_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Part one: {part_one(puzzle_input)}')
