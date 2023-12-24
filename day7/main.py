from collections import Counter
from typing import TextIO


def read_play(file: TextIO):
    for line in file:
        hand, bit = line.strip().split(" ")
        yield hand, int(bit)


def card_ranks(hand: str, joker_value=11):
    card_values = []
    for card in hand:
        if card.isdigit():
            card_values.append(int(card))
        elif card == 'T':
            card_values.append(10)
        elif card == 'J':
            card_values.append(joker_value)
        elif card == 'Q':
            card_values.append(12)
        elif card == 'K':
            card_values.append(13)
        elif card == 'A':
            card_values.append(14)
    return card_values


def hand_strength(hand: str):
    counts = Counter(hand)
    if len(counts) == 1:
        return 7  # Five of a Kind
    elif len(counts) == 2 and 4 in counts.values():
        return 6  # Four of a Kind
    elif len(counts) == 2:
        return 5  # Full House
    elif len(counts) == 3 and 3 in counts.values():
        return 4  # Three of a Kind
    elif len(counts) == 3:
        return 3  # Two Pairs
    elif len(counts) == 4:
        return 2  # One Pair
    else:
        return 1  # High Card


def replace_jokers(hand: str):
    counts = Counter(hand)
    if "J" not in counts:
        return hand

    most_frequent_card = ("", 0)
    for card, count in counts.items():
        if card != "J" and count > most_frequent_card[1]:
            most_frequent_card = (card, count)

    if not most_frequent_card[0]:
        return hand

    return hand.replace("J", most_frequent_card[0])


def part1(file_path):
    with open(file_path, 'r') as file:
        plays = read_play(file)

        def order_key(play):
            return hand_strength(play[0]), card_ranks(play[0])

        sorted_plays = sorted([(hand, bit) for hand, bit in plays], key=order_key)
        return sum([rank * x[1] for rank, x in enumerate(sorted_plays, start=1)])


def part2(file_path):
    with open(file_path, 'r') as file:
        plays = read_play(file)

        def order_key(play):
            return hand_strength(replace_jokers(play[0])), card_ranks(play[0], joker_value=1)

        sorted_plays = sorted([(hand, bit) for hand, bit in plays], key=order_key)
        return sum([rank * x[1] for rank, x in enumerate(sorted_plays, start=1)])


if __name__ == '__main__':
    res = part2('input.txt')
    print(res)
