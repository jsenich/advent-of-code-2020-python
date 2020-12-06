import itertools
import math
from typing import List, Tuple


def find_entries(expense_report: List[str], num_entries: int) -> Tuple[int]:
    for expenses in itertools.combinations(expense_report, num_entries):
        if sum(expenses) == 2020:
            return expenses


if __name__ == '__main__':
    with open('day01_input.txt') as f:
        expense_report = [int(n) for n in f.readlines()]

    day1_entries = find_entries(expense_report, 2)
    day2_entries = find_entries(expense_report, 3)

    print(f'Day 1 - Part 1: ({" * ".join([str(e) for e in day1_entries])}) = {math.prod(day1_entries)}')
    print(f'Day 1 - Part 2: ({" * ".join([str(e) for e in day2_entries])}) = {math.prod(day2_entries)}')
