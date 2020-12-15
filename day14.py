import re
from collections import defaultdict


def part_one(puzzle_input):
    memory = defaultdict(int)
    mask = None
    for line in puzzle_input.split('\n'):
        key, value = line.split(' = ')
        if key == 'mask':
            mask = value
            continue
        mem_location = int(re.findall(r'\d+', key)[0])
        bit_value = list(format(int(value), '036b'))
        for i, bit in enumerate(mask):
            if bit in ('1', '0'):
                bit_value[i] = mask[i]
        memory[mem_location] = int(''.join(bit_value), 2)

    return sum(memory.values())


if __name__ == "__main__":
    test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

    with open('day14_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Part 1: {part_one(puzzle_input)}')
