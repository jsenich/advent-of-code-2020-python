import math
from day01 import find_entries


expense_report = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

def test_part_one():
    entries = find_entries(expense_report, 2)
    assert {1721, 299} == set(entries)
    assert 514579 == math.prod(entries)

def test_part_two():
    entries = find_entries(expense_report, 3)
    assert {979, 366, 675} == set(entries)
    assert 241861950 == math.prod(entries)