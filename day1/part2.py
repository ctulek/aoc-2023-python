from typing import TextIO
from unittest import TestCase

patterns = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def get_digit(line: str):
    if line[0].isdigit():
        return int(line[0])

    for i, pattern in enumerate(patterns):
        if line.startswith(pattern):
            return i

    return None


def first_and_last_digit(line: str):
    first = None
    last = None
    for i in range(len(line)):
        n = get_digit(line[i:])
        if n:
            if not first:
                first = n
                last = n
            else:
                last = n

    return first, last


def calibration_values(f: TextIO):
    for line in f:
        (first, last) = first_and_last_digit(line)
        # print(first, last, line)
        yield first * 10 + last


def main(file_name: str):
    with open(file_name, "r") as f:
        return sum(calibration_values(f))


if __name__ == '__main__':
    res = main("input.txt")
    print(res)


class Test(TestCase):
    def test_example(self):
        self.assertEqual(281, main("part2_test_input.txt"))
