

def part_one(puzzle_input):
    ticket_rules, ticket, nearby = puzzle_input.split('\n\n')

    errors = []
    rule_ranges = []
    for line in ticket_rules.strip().split('\n'):
        _, range_args = line.split(': ')
        for r in range_args.split(' or '):
            start, stop = r.split('-')
            rule_ranges.append([int(start), int(stop) + 1])

    for i, ticket in enumerate(nearby.strip().split('\n')):
        if i == 0:
            continue
        nums = [int(n) for n in ticket.split(',')]
        for num in nums:
            failures = 0
            for rule in rule_ranges:
                if num not in range(rule[0], rule[1]):
                    failures += 1
            if failures == len(rule_ranges):
                errors.append(num)

    return sum(errors)


if __name__ == "__main__":
    test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

    with open('day16_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Part 1: {part_one(puzzle_input)}')
