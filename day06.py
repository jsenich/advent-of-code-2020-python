
if __name__ == '__main__':
    test_input = """abcx
abcy
abcz
"""
    with open('day06_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    group_counts = []
    for group in puzzle_input.split('\n\n'):
        unique_answers = set()
        for line in group.split():
            unique_answers.update(line)
        group_counts.append(len(unique_answers))

    print(f'summed counts: {sum(group_counts)}')

    group_counts = []
    for group in puzzle_input.split('\n\n'):
        group_answers = []
        for person in group.split():
            group_answers.append(set(person))
        group_counts.append(len(set.intersection(*group_answers)))

    print(f'summed counts: {sum(group_counts)}')
