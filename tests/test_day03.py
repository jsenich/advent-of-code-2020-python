from day03 import part_one, part_two


puzzle_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

def test_part_one():
    slope = (3, 1)
    assert 7 == part_one(puzzle_input, slope)

def test_part_two():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    assert 336 == part_two(puzzle_input, slopes)
