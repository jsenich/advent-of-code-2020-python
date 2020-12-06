from typing import List


def part_one(puzzle_input: str) ->  List[int]:
    group_counts = []
    for group in puzzle_input.split('\n\n'):
        unique_answers = set()
        for person in group.split():
            unique_answers.update(person)
        group_counts.append(len(unique_answers))

    return group_counts


def part_two(puzzle_input: str) -> List[int]:
    group_counts = []
    for group in puzzle_input.split('\n\n'):
        group_answers = []
        for person in group.split():
            group_answers.append(set(person))
        group_counts.append(len(set.intersection(*group_answers)))

    return group_counts


if __name__ == '__main__':
    with open('day06_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    print(f'Day 1 counts: {sum(part_one(puzzle_input))}')

    print(f'Day 2 counts: {sum(part_two(puzzle_input))}')
