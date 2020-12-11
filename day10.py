from collections import Counter, defaultdict
from typing import Dict, List

test_input = """16
10
15
5
1
11
7
19
6
12
4
"""


def part_one(puzzle_input: List[int]) -> Dict[str, int]:
    joltages = sorted(puzzle_input)
    adapter_pointer = 0
    adapter_rating = max(joltages) + 3
    previous_output = 0
    used_adapters = set()
    differences = Counter()

    joltages.append(adapter_rating)

    current_adapter = joltages[adapter_pointer]
    while current_adapter not in used_adapters:
        if adapter_pointer > len(joltages):
            adapter_pointer = 0
            continue

        if joltages[adapter_pointer] - 3 <= previous_output:
            used_adapters.add(joltages[adapter_pointer])
            differences.update(str(joltages[adapter_pointer] - previous_output))
            previous_output = joltages[adapter_pointer]
            if adapter_pointer + 1 < len(joltages):
                current_adapter = joltages[adapter_pointer + 1]
        adapter_pointer += 1

    return dict(differences)


def part_two(puzzle_input: List[int]) -> int:
    joltages = sorted([0] + puzzle_input + [max(puzzle_input) + 3])

    variations_map = defaultdict(list)
    for i, joltage in enumerate(joltages):
        variations = []
        for jolt_diff in range(1, 4):
            variations.append(joltage + jolt_diff)
        for joltage2 in joltages:
            if joltage2 in variations:
                variations_map[joltage].append(joltage2)

    adapter_combinations = defaultdict(int)
    adapter_combinations[0] = 1
    for joltage, variations in variations_map.items():
        for variation in variations:
            adapter_combinations[variation] += adapter_combinations[joltage]

    return adapter_combinations[max(joltages)]


if __name__ == '__main__':
    with open('day10_input.txt', 'r') as f:
        puzzle_input = [int(i) for i in f.read().strip().split()]
        test_input = [int(i) for i in test_input.strip().split()]

    differences = part_one(puzzle_input)

    print(f'Part 1: {differences["1"] * differences["3"]}')
    print(part_two(puzzle_input))
