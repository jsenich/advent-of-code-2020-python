import pytest
from day05 import get_seat_row, get_seat_number, part_one


@pytest.mark.parametrize('seat_code, expected', [
    ('FBFBBFFRLR', 44),
    ('BFFFBBFRRR', 70),
    ('FFFBBBFRRR', 14),
    ('BBFFBBFRLL', 102),
])
def test_get_seat_row(seat_code, expected):
    assert expected == get_seat_row(seat_code)


@pytest.mark.parametrize('seat_code, expected', [
    ('FBFBBFFRLR', 5),
    ('BFFFBBFRRR', 7),
    ('FFFBBBFRRR', 7),
    ('BBFFBBFRLL', 4),
])
def test_get_seat_number(seat_code, expected):
    assert expected == get_seat_number(seat_code)


@pytest.mark.parametrize('seat_code, expected', [
    ('FBFBBFFRLR', 357),
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
])
def test_part_one(seat_code, expected):
    assert expected == part_one(seat_code)
