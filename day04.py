import re
from typing import Dict, List, Tuple


def get_passports_from_input(puzzle_input:str) -> List[Dict[str, str]]:
    parsed_passports = []
    for passport in puzzle_input.split('\n\n'):
        passport_dict = {}
        for field, field_value in (f.split(':') for f in passport.split()):
            passport_dict[field] = field_value
        parsed_passports.append(passport_dict)

    return parsed_passports


def validate_field(field_name: str, field_value: str) -> bool:
    if field_name in ('byr', 'iyr', 'eyr'):
        field_value = int(field_value)

        if field_name == 'byr' and 1920 <= field_value <= 2002:
            return True
        if field_name == 'iyr' and 2010 <= field_value <= 2020:
            return True
        if field_name == 'eyr' and 2020 <= field_value <= 2030:
            return True
    elif field_name == 'hgt':
        unit = field_value[-2:]
        if unit in ('cm', 'in'):
            height = field_value[:-2]
            height = int(height)
            if unit == 'cm' and 150 <= height <= 193:
                return True
            elif unit == 'in' and 59 <= height <= 76:
                return True
    if field_name == 'pid':
        if len(field_value) == 9 and all(s.isdigit() for s in field_value):
            return True
    if field_name == 'ecl':
        if len(field_value.strip()) == 3 and field_value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return True
    if field_name == 'hcl':
        if len(field_value) == 7  and re.match(r'^#[0-9a-f]{6}$', field_value):
            return True
    return False

def part_one(puzzle_input: str, required_fields: Tuple[str]) -> int:
    valid_passports_count = 0
    for passport in get_passports_from_input(puzzle_input):
        passport_fields = set(passport.keys())
        if 'cid' in passport_fields:
            passport_fields.remove('cid')
        if passport_fields == required_fields:
            valid_passports_count += 1
    return valid_passports_count

def part_two(puzzle_input: str, required_fields: Tuple[str]):
    valid_passports_count = 0
    for passport in get_passports_from_input(puzzle_input):
        is_valid = True
        # Passport contains all required fields
        if not all(f in passport for f in required_fields):
            continue

        is_valid = all(validate_field(field, passport[field]) for field in required_fields)

        if is_valid:
            valid_passports_count += 1

    return valid_passports_count

if __name__ == '__main__':
    with open('day04_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    print(f'Part 1 Valid Passports: {part_one(puzzle_input, required_fields)}')

    print(f'Part 2 Valid Passports: {part_two(puzzle_input, required_fields)}')
