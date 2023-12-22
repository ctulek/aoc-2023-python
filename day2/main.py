import operator
from functools import reduce
from typing import TextIO
from unittest import TestCase


def read_game(file: TextIO):
    for line in file:
        [game, data] = line.split(":")
        game = int(game.split(" ")[1])
        draws = data.split(";")
        yield game, map(read_draw, draws)


def read_draw(draw_str: str):
    colors = draw_str.strip().split(", ")
    draw = {}
    for number_and_color in colors:
        [n, color] = number_and_color.split(" ")
        draw[color] = int(n)
    return draw


def can_be_played(draw, limits):
    for color, n in draw.items():
        if limits[color] < n:
            return False

    return True


def part1(file_path, limits):
    with open(file_path, "r") as file:
        ans = 0
        for game, draws in read_game(file):
            if all([can_be_played(draw, limits) for draw in draws]):
                ans += game
        return ans


def min_needed(draws):
    max_numbers = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for draw in draws:
        for color, n in draw.items():
            max_numbers[color] = max(max_numbers[color], n)

    return max_numbers


def part2(file_path, limits):
    with open(file_path, "r") as file:
        ans = 0
        for game, draws in read_game(file):
            values = min_needed(draws).values()
            ans += reduce(operator.mul, values, 1)
        return ans


if __name__ == '__main__':
    res = part2("input.txt", {'red': 12, 'green': 13, 'blue': 14})
    print(res)


class Test(TestCase):
    def test_part1(self):
        res = part1("test_input.txt", {'red': 12, 'green': 13, 'blue': 14})
        self.assertEqual(8, res)

    def test_part2(self):
        res = part2("test_input.txt", {'red': 12, 'green': 13, 'blue': 14})
        self.assertEqual(2286, res)
