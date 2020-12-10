from typing import List, Set, Tuple


class Program:
    def __init__(self, instructions: List[Tuple[str, int]]) -> None:
        self.instructions = instructions
        self.executed_pointers: Set[int] = set()
        self.change_attempted: Set[int] = set()

        self.accumulator: int
        self.instruction_pointer: int
        self.memory: List[Tuple[str, int]]

        self.initialize()

    def initialize(self) -> None:
        self.accumulator = 0
        self.executed_pointers.clear()
        self.instruction_pointer = 0
        self.memory = self.instructions.copy()

    def run(self, correct_errors: bool = False) -> Tuple[int, int]:
        while self.instruction_pointer < len(self.memory):
            if self.instruction_pointer in self.executed_pointers:
                if correct_errors:
                    self.initialize()
                else:
                    return 1, self.accumulator

            self.executed_pointers.add(self.instruction_pointer)

            op, argument = self.memory[self.instruction_pointer]

            if op == 'acc':
                self._execute_acc(argument)
            elif op == 'jmp':
                self._execute_jmp(argument)
            else:  # nop
                self._execute_nop()

        return 0, self.accumulator

    def _execute_acc(self, argument: int) -> None:
        self.accumulator += argument
        self.instruction_pointer += 1

    def _execute_jmp(self, argument: int) -> None:
        self.accumulator += argument

    def _execute_nop(self) -> None:
        self.instruction_pointer += 1


def get_instructions(puzzle_input: str) -> List[Tuple[str, int]]:
    instructions = []
    for line in puzzle_input.strip().split('\n'):
        op, arg = line.split(' ')
        instructions.append((op, int(arg)))
    return instructions


def part_one(puzzle_input) -> int:
    program = Program(get_instructions(puzzle_input))
    _, accumulator = program.run(correct_errors=False)

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
