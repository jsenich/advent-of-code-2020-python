import re
import itertools
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


def part_two(puzzle_input):
#     puzzle_input = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1"""

    memory = defaultdict(int)
    mask = None
    for line in puzzle_input.split('\n'):
        key, value = line.split(' = ')
        if key == 'mask':
            mask = value
            continue
        mem_location = int(re.findall(r'\d+', key)[0])
        bit_value = list(format(int(mem_location), '36b').strip())
        mask = mask[len(mask) - len(bit_value)::]
        for i, bit in enumerate(mask):
            if bit in ('1', 'X'):
                bit_value[int(i)] = mask[i]

        floating_count = bit_value.count('X')
        for comb in itertools.product(range(2), repeat=floating_count):
            comb = list(comb)
            bit_value2 = bit_value.copy()
            for i, ival in enumerate(bit_value2):
                if ival == 'X':
                    bit_value2[i] = str(comb.pop(0))
            memory[int(''.join(bit_value2), 2)] = int(value)

    return sum(memory.values())


if __name__ == "__main__":
    test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

    with open('day14_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    # print(f'Part 1: {part_one(puzzle_input)}')
    print(f'Part 2: {part_two(puzzle_input)}')
