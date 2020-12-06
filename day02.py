from collections import Counter
from typing import List, Tuple


def check_frequency_policy(password: str, policy_character: str, args: List[str]) -> bool:
    low, high = args
    character_counts = Counter(password)

    return int(low) <= character_counts.get(policy_character, 0) <= int(high)


def check_position_policy(password: str, policy_character: str, args: List[str]) -> bool:
    position1, position2 = args
    password_characters = [password[int(position1) - 1], password[int(position2) - 1]]
    character_counts = Counter(password_characters)

    return character_counts.get(policy_character, 0) == 1


def get_parsed_policy_line(password_line: str) -> Tuple[str, str, List[str]]:
    policy_params, password = password_line.split(': ')
    policy_args, letter = policy_params.split()

    return password, letter, policy_args.split('-')


def part_one(puzzle_input: List[str]) -> int:
    valid_passwords = []
    for line in puzzle_input:
        password, letter, args = get_parsed_policy_line(line)
        if check_frequency_policy(password, letter, args):
            valid_passwords.append(password)

    return len(valid_passwords)


def part_two(puzzle_input: List[str]) -> int:
    valid_passwords = []
    for line in puzzle_input:
        password, letter, args = get_parsed_policy_line(line)
        if check_position_policy(password, letter, args):
            valid_passwords.append(password)

    return len(valid_passwords)


if __name__ == '__main__':
    with open('day02_input.txt', 'r') as f:
        puzzle_input = [line for line in f.readlines() if line]

    print(f'Part 1 Valid Passwords: {part_one(puzzle_input)}')

    print(f'Part 2 Valid Passwords: {part_two(puzzle_input)}')
