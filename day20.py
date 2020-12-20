import re
import operator

from functools import reduce
from collections import defaultdict
from typing import List

import numpy as np

test_input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""


def parse_input(puzzle_input: str) -> dict:
    tiles = {}
    for tile_parts in puzzle_input.split('\n\n'):
        image_id = None
        image = []
        for i, part in enumerate(tile_parts.split('\n')):
            if i == 0:
                image_id = int(re.sub(r'[a-zA-Z\s\:]', '', part))
                continue
            image.append(list(part))
        tiles[image_id] = np.array(image)
    return tiles


def find_corners(image_tiles: dict) -> List[int]:
    # square_size = int(math.sqrt(len(image_tiles)))

    match_counts = defaultdict(int)

    for image_id1 in image_tiles:
        for image_id2 in image_tiles:
            if image_id2 == image_id1:
                continue
            if (
                list(image_tiles[image_id1][:, -1]) == list(image_tiles[image_id2][:, 0]) or
                list(image_tiles[image_id1][:, 0]) == list(image_tiles[image_id2][:, -1]) or
                list(image_tiles[image_id1][-1]) == list(image_tiles[image_id2][0]) or
                list(image_tiles[image_id1][0]) == list(image_tiles[image_id2][-1])
            ):
                match_counts[image_id1] += 1
                continue
            h_flip = np.fliplr(image_tiles[image_id2])
            v_flip = np.flipud(image_tiles[image_id2])
            if (
                list(image_tiles[image_id1][:, -1]) == list(h_flip[:, 0]) or
                list(image_tiles[image_id1][:, 0]) == list(h_flip[:, -1]) or
                list(image_tiles[image_id1][-1]) == list(v_flip[0]) or
                list(image_tiles[image_id1][0]) == list(v_flip[-1])
            ):
                match_counts[image_id1] += 1
                continue

            for i, _ in enumerate(range(3), 1):
                rot = np.rot90(image_tiles[image_id2], i)
                if (
                    list(image_tiles[image_id1][:, -1]) == list(rot[:, 0]) or
                    list(image_tiles[image_id1][:, 0]) == list(rot[:, -1]) or
                    list(image_tiles[image_id1][-1]) == list(rot[0]) or
                    list(image_tiles[image_id1][0]) == list(rot[-1])
                ):
                    match_counts[image_id1] += 1
                    continue
                h_flip = np.fliplr(rot)
                v_flip = np.flipud(rot)
                if (
                    list(image_tiles[image_id1][:, -1]) == list(h_flip[:, 0]) or
                    list(image_tiles[image_id1][:, 0]) == list(h_flip[:, -1]) or
                    list(image_tiles[image_id1][-1]) == list(v_flip[0]) or
                    list(image_tiles[image_id1][0]) == list(v_flip[-1])
                ):
                    match_counts[image_id1] += 1
                    continue

            notmatched = 'here'
    corners = [_id for _id in match_counts if match_counts[_id] == 2]

    return corners


def part_one(puzzle_input):
    tiles = parse_input(puzzle_input)

    return reduce(operator.__mul__, find_corners(tiles))


if __name__ == '__main__':
    with open('day20_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    # puzzle_input = test_input.strip()

    print(f'Part 1: {part_one(puzzle_input)}')

