import pytest

from day02 import part_one, part_two

puzzle_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

puzzle_input_with_dupes = [
    "2-4 a: aabbbb",
    "1-5 a: aabbbb",
    "1-5 b: qwerty",
]

@pytest.mark.parametrize("test_input, expected", [
    (puzzle_input, 2),
    (puzzle_input_with_dupes, 2)
    ]
)
def test_part_one(test_input, expected):
    assert expected == part_one(test_input)

@pytest.mark.parametrize("test_input, expected", [
    (puzzle_input, 1),
    (puzzle_input_with_dupes, 2)
    ]
)
def test_part_two(test_input, expected):
    assert expected == part_two(test_input)
