from collections import Counter

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



if __name__ == '__main__':
    with open('day10_input.txt', 'r') as f:
        puzzle_input = [int(i) for i in f.read().strip().split()]


    # adapters = sorted([int(n) for n in test_input.strip().split('\n')])
    adapters = sorted(puzzle_input)
    adapter_pointer = 0
    adapter_rating = max(adapters) + 3
    previous_output = 0
    used_adapters = set()
    differences = Counter()

    adapters.append(adapter_rating)

    current_adapter = adapters[adapter_pointer]
    while current_adapter not in used_adapters:
        if adapter_pointer > len(adapters):
            adapter_pointer = 0
            continue

        if adapters[adapter_pointer] - 3 <= previous_output:
            used_adapters.add(adapters[adapter_pointer])
            differences.update(str(adapters[adapter_pointer] - previous_output))
            previous_output = adapters[adapter_pointer]
            if adapter_pointer + 1 < len(adapters):
                current_adapter = adapters[adapter_pointer + 1]
        adapter_pointer += 1

    print(f'Part 1: {differences["1"] * differences["3"]}')
