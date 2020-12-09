import itertools

test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


if __name__ == '__main__':
    with open('day09_input.txt', 'r') as f:
        puzzle_input = [int(i) for i in f.read().strip().split()]
        # puzzle_input = [int(i) for i in test_input.strip().split()]

        premble_length = 25
        start = premble_length
        premble = puzzle_input[0:premble_length]
        day_one_answer = 0
        while True:
            if not any(sum(comb) == puzzle_input[start] for comb in itertools.combinations(premble[-premble_length:], 2)):
                day_one_answer = puzzle_input[start]
                print(f'Part 1: {day_one_answer}')
                break
            premble.append(puzzle_input[start])
            start += 1

        previous_numbers = puzzle_input[0:start]
        for i in range(2, len(premble)):
            for j in range(len(premble)):
                if sum(premble[j:j+i]) == day_one_answer:
                    print(f'Part 2: {sum([min(premble[j:j+i]), max(premble[j:j+i])])}')
                    break
