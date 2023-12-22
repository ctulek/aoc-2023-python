from collections import defaultdict
from typing import TextIO


def card_matches(f: TextIO):
    for line in f:
        line = line.split(":")[1].strip()
        winners, candidates = line.split("|")
        winners = filter(lambda x: len(x) > 0, winners.strip().split(" "))
        candidates = filter(lambda x: len(x) > 0, candidates.strip().split(" "))
        winners = set(map(int, winners))
        candidates = set(map(int, candidates))
        # print(list(winners), list(candidates))

        matches = candidates.intersection(winners)
        # print(matches)
        # print(2 ** (len(matches) - 1))
        yield len(matches)


def part1(file_path: str):
    with open(file_path, "r") as f:
        return sum(2 ** (v - 1) if v > 0 else 0 for v in card_matches(f))


def part2(file_path: str):
    with open(file_path, "r") as f:
        card_counts = defaultdict(int)
        card_number = 0
        for value in card_matches(f):
            card_number += 1
            card_counts[card_number] += 1
            print(card_number, value, card_counts[card_number])
            for _ in range(card_counts[card_number]):
                for i in range(card_number + 1, card_number + value + 1):
                    card_counts[i] += 1
        return sum(card_counts.values())


if __name__ == '__main__':
    res = part2("input.txt")
    print(res)