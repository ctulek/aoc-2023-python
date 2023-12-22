from typing import TextIO
from unittest import TestCase


def first_and_last_digit(line: str):
    first = None
    last = None
    for c in line:
        if c.isdigit():
            if not first:
                first = int(c)
                last = int(c)
            else:
                last = int(c)

    return first, last


def calibration_values(f: TextIO):
    for line in f:
        (first, last) = first_and_last_digit(line)
        yield first * 10 + last


def main(file_name: str):
    with open(file_name, "r") as f:
        return sum(calibration_values(f))


if __name__ == '__main__':
    res = main("input.txt")
    print(res)


class Test(TestCase):
    def test_example(self):
        self.assertEqual(142, main("part1_test_input.txt"))
