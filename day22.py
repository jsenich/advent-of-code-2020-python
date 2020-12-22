
from typing import List, Tuple


test_input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


def parse_decks(puzzle_input) -> Tuple[List[int], List[int]]:
    decks = {}
    for deck in puzzle_input.split('\n\n'):
        player = None
        for card in deck.split('\n'):
            if not player:
                player = card
            else:
                decks.setdefault(player, []).append(int(card))

    return list(decks.values())[0], list(decks.values())[1]


def part_one(p1_deck: List[int], p2_deck: List[int]):
    rounds = 1
    while True:
        if len(p1_deck) == 0 or len(p2_deck) == 0:
            break

        c1 = p1_deck.pop(0)
        c2 = p2_deck.pop(0)

        if c1 == c2:
            p1_deck.append(c1)
            p2_deck.append(c2)
        elif c1 > c2:
            p1_deck.extend([c1, c2])
        else:
            p2_deck.extend([c2, c1])

        rounds += 1

    winner = p1_deck if len(p1_deck) else p2_deck

    total = 0
    for i, card in enumerate(winner, -len(winner)):
        total += abs(i) * card

    return total


if __name__ == "__main__":
    with open('day22_input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    # puzzle_input = test_input.strip()

    print(f'Part 1: {part_one(*parse_decks(puzzle_input))}')
