import operator
import re
from functools import reduce
from operator import add, mul


test_input = """1 + 2 * 3 + 4 * 5 + 6
"""

test_input = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

test_input = """(2 + 7 * (3 + 5 * 2 + 3 + 6) * (4 * 6 + 8 * 3 * 2 + 7)) + 3 * ((2 + 8 + 6) * 8 + 9 * 6 * 6) + 5 + 6 + 5
"""

#  ((6 * 9) * (15 * 14) + 6) + 6 * 2
#  (54 * 210 + 6) + 6 * 2
#  (54 * 216) + 6 * 2
#  11664 + 6 * 2
#  11670 * 2
#  23340


# test_input = """1 + (2 * 3) + (4 * (5 + 6))
# """

op_map = {
    '+': add,
    '*': mul,
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


def process_additions(expression_string: str):
    expression = expression_string
    while additions := re.findall(r'\d+\s\+\s\d+(?:\s\+\s\d+)*', expression):
        for addition in additions:
            nums = [int(num) for num in addition.split(' + ')]
            expression = expression.replace(addition, str(sum(nums)).replace('(', '').replace(')', ''))
    return expression


def process_products(expression_string: str):
    expression = expression_string
    while products := re.findall(r'\d+\s\*\s\d+(?:\s\*\s\d+)*', expression):
        for product in products:
            nums = [int(num) for num in product.split(' * ')]
            expression = expression.replace(product, str(reduce(operator.__mul__, nums)).replace('(', '').replace(')', ''))
    return expression


def strip_noop_expressions(expression_string: str):
    expression = expression_string
    while noops := re.findall(r'\(\d+\)', expression):
        for noop in noops:
            expression = expression.replace(noop, noop.replace('(', '').replace(')', ''))

    return expression

# (2 + 7 * (3 + 5 * 2 + 3 + 6) * (4 * 6 + 8 * 3 * 2 + 7)) + 3 * ((2 + 8 + 6) * 8 + 9 * 6 * 6) + 5 + 6 + 5
# (9 * (8 * 11) * (4 * 14 * 3 * 9)) + 3 * (16 * 17 * 6 * 6) + 16
# (9 * 88 * 1512) + 3 * 9792 + 16
# 1197504 + 3 * 9808
# 1197507 * 9808
# 11745148656



def part_two(puzzle_input: str):
    result = 0
    for expression in puzzle_input.strip().split('\n'):
        processing = True
        while processing:
            # if expression.count('(') <= 1:
            #     expression = re.sub(r'[\(\)]', '', expression)
            #     processing = False
            #     continue

            if subexpressions := re.findall(r'\([\d\s\+\*]+\)', expression):
                for subexpression in subexpressions:
                    new_expression = process_products(process_additions(subexpression))
                    if re.match(r'^\(\d+\)$', new_expression):
                        new_expression = re.sub(r'[\(\)]', '', new_expression)
                    expression = expression.replace(subexpression, new_expression)
            else:
                processing = False
            # print(expression)
        result += int(process_products(process_additions(expression)))

    return result


if __name__ == '__main__':
    with open('day18_input.txt', 'r') as f:
        puzzle_input = f.read()
    # puzzle_input = test_input.strip()

    print(f'Part 1: {part_one(puzzle_input)}')
    print(f'Part 2: {part_two(puzzle_input)}')
