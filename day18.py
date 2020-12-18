import operator, re

test_input = """1 + 2 * 3 + 4 * 5 + 6
"""

test_input = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

op_map = {
    '+': operator.add,
    '*': operator.mul,
}


def evaluate_expression_string(expression_string: str):
    expression = expression_string.replace('(', '').replace(')', '').split()
    result = None

    curr_pos = 0
    while curr_pos < len(expression) - 1:
        if curr_pos == 0:
            result = int(expression[curr_pos])
            curr_pos += 1
            continue
        if expression[curr_pos] in ('*', '+'):
            result = op_map[expression[curr_pos]](result, int(expression[curr_pos+1]))
            curr_pos = curr_pos + 2

    return result

def part_one(puzzle_input):
    result = 0
    for expression in puzzle_input.strip().split('\n'):
        while (expressions := re.findall(r'\([\d\s\+\*]+\)', expression)):
            for exp in expressions:
                expression = expression.replace(exp, str(evaluate_expression_string(exp)))
        result += evaluate_expression_string(expression)

    return result


if __name__ == '__main__':
    with open('day18_input.txt', 'r') as f:
        puzzle_input = f.read()
    # puzzle_input = test_input.strip()

    print(f'Part 1: {part_one(puzzle_input)}')
