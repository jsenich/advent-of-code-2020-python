
def part_one(puzzle_input) -> int:
    accumulator = 0
    instruction_pointer = 0
    instructions = puzzle_input.strip().split('\n')
    visited = set()
    while instruction_pointer not in visited:
        visited.add(instruction_pointer)
        op, argument = instructions[instruction_pointer].split(' ')

        if op == 'nop':
            instruction_pointer += 1
            continue

        if op == 'acc':
            accumulator += int(argument)
            instruction_pointer += 1
        elif op == 'jmp':
            instruction_pointer += int(argument)

    return accumulator


def part_two(puzzle_input: str) -> int:
    accumulator = 0
    instruction_pointer = 0
    instructions = puzzle_input.strip().split('\n')
    memory = instructions.copy()
    visited = set()
    change_attempted = set()
    program_changed = False

    def reset_instructions():
        nonlocal memory, accumulator, instruction_pointer, program_changed
        memory = instructions.copy()
        accumulator = 0
        instruction_pointer = 0
        visited.clear()
        program_changed = False

    while instruction_pointer < len(memory):
        if instruction_pointer in visited:
            reset_instructions()
            continue

        op, argument = memory[instruction_pointer].split(' ')

        visited.add(instruction_pointer)
        if op == 'nop':
            if program_changed:
                instruction_pointer += 1
                continue
            else:
                if instruction_pointer not in change_attempted:
                    change_attempted.add(instruction_pointer)
                    memory[instruction_pointer] = memory[instruction_pointer].replace('nop', 'jmp')
                    instruction_pointer += int(argument)
                    program_changed = True
                else:
                    instruction_pointer += 1
                continue

        if op == 'acc':
            accumulator += int(argument)
            instruction_pointer += 1
        elif op == 'jmp':
            if program_changed:
                instruction_pointer += int(argument)
            else:
                if instruction_pointer not in change_attempted:
                    memory[instruction_pointer] = memory[instruction_pointer].replace('jmp', 'nop')
                    change_attempted.add(instruction_pointer)
                    instruction_pointer += 1
                    program_changed = True
                else:
                    instruction_pointer += int(argument)

    return accumulator


if __name__ == '__main__':
    with open('day08_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    value = part_one(puzzle_input)
    value2 = part_two(puzzle_input)

    print(f'Part 1: {value}')
    print(f'Part 2: {value2}')
