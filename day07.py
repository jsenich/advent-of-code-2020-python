from typing import Dict, List, Tuple


def get_bag_rules(puzzle_input: str) -> Dict[str, List[Tuple[int, str]]]:
    rules = {}
    for line in puzzle_input.split('\n'):
        main_bag, child_bags = line.split(' bags contain ')

        for bag in child_bags.split(', '):
            if bag.startswith('no other'):
                rules.setdefault(main_bag,  [])
                continue
            bag = bag.replace('.', '').replace(' bags', '').replace('bag', '').strip()
            rules.setdefault(main_bag, []).append(tuple(bag.split(' ', 1)))

    return rules


def get_parent_count_for_color(bag_rules: Dict[str, List[Tuple[int, str]]], target_color: str) -> int:
    parents = {}

    for parent_bag, child_bags in bag_rules.items():
        for bag in child_bags:
            parents.setdefault(bag[1], []).append(parent_bag)

    def walk_parents(color: str) -> set:
        # counter = 0
        processed = set()
        for parent_color in parents.get(color) or []:
            # counter += 1
            processed.add(parent_color)
            processed.update(walk_parents(parent_color))

        return processed

    return len(walk_parents(target_color))


def get_child_counts(bag_rules: Dict[str, List[Tuple[int, str]]], target_color: str):
    def walk_bags(color: str):
        total = 0
        for count, bag in bag_rules[color]:
            total += int(count) + int(count) * walk_bags(bag)
        return total

    return walk_bags(target_color)


if __name__ == '__main__':
    with open('day07_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    bag_rules = get_bag_rules(puzzle_input)

    # buld_child_bags(bag_map)
    print(f'Part 1: {get_parent_count_for_color(bag_rules, "shiny gold")}')
    print(f'Part 2: {get_child_counts(bag_rules, "shiny gold")}')
