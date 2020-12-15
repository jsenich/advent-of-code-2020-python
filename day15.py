from collections import defaultdict
from functools import reduce
import operator
import itertools
from typing import List


def part_one(numbers: List[int], stop_turn: int):
    last_spoken = 0
    spoken_numbers = defaultdict(list)
    for turn, num in enumerate(numbers, 1):
        spoken_numbers[num].append(turn)
        last_spoken = num

    for turn in itertools.count(len(numbers) + 1, 1):
        spoken_count = len(spoken_numbers[last_spoken])
        if spoken_count == 1:
            last_spoken = 0
        if spoken_count > 1:
            last_spoken = reduce(operator.__sub__, spoken_numbers[last_spoken][-1:-3:-1])
            if last_spoken == 0:
                last_spoken = 1
        spoken_numbers[last_spoken].append(turn)

        if turn == stop_turn:
            return last_spoken

if __name__ == "__main__":
    # test_input = '0,3,6'
    puzzle_input = '0,8,15,2,12,1,4'

    numbers = [int(n) for n in puzzle_input.split(',')]

    print(f'Part 1: {part_one(numbers, 2020)}')
    print(f'Part 2: {part_one(numbers, 30_000_000)}')
