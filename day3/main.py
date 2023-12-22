from typing import TextIO
from unittest import TestCase


def next_or_none(f):
    try:
        r = next(f)
        return r
    except:
        return None


def three_lines(f):
    prev = None
    next_line = next_or_none(f)
    while next_line:
        curr = next_line
        next_line = next_or_none(f)
        yield prev, curr, next_line
        prev = curr


def is_symbol(line: str, i):
    if not line:
        return False
    if 0 <= i < len(line):
        return not line[i].isdigit() and line[i] != "." and not line[i].isspace()

    return False


def is_part_number(start, end, line, prev_line, next_line):
    if is_symbol(line, start - 1) or is_symbol(line, end + 1):
        return True

    for i in range(start - 1, end + 2):
        if is_symbol(prev_line, i) or is_symbol(next_line, i):
            return True

    return False


def part_number(line: str, prev_line, next_line):
    n = 0
    start = 0
    end = 0
    for i, c in enumerate(line):
        if c.isdigit():
            end = i
            n = n * 10 + int(c)
        else:
            if n > 0 and is_part_number(start, end, line, prev_line, next_line):
                yield n
            n = 0
            start = i + 1

    if n > 0 and is_part_number(start, end, line, prev_line, next_line):
        yield n


def part_numbers(f):
    num_line = 0
    for prev, curr, next_line in three_lines(f):
        num_line += 1
        numbers = []
        for n in part_number(curr, prev, next_line):
            numbers.append(n)
            yield n
        print(num_line, numbers)


def add_number(line: str, i: int, numbers: set):
    if 0 <= i < len(line):
        if line[i].isdigit():
            left = right = i
            while left > 0 and line[left - 1].isdigit():
                left -= 1
            while right < len(line) - 1 and line[right + 1].isdigit():
                right += 1
            numbers.add(int(line[left:right + 1]))


def gear_ratio(line, prev_line, next_line):
    for i, c in enumerate(line):
        numbers = set()
        if c == "*":
            add_number(line, i - 1, numbers)
            add_number(line, i + 1, numbers)
            for j in range(i - 1, i + 2):
                add_number(prev_line, j, numbers)
                add_number(next_line, j, numbers)

        if len(numbers) == 2:
            numbers = list(numbers)
            yield numbers[0] * numbers[1]


def gear_ratios(f: TextIO):
    num_line = 0
    for prev, curr, next_line in three_lines(f):
        num_line += 1
        ratios = []
        for r in gear_ratio(curr, prev, next_line):
            ratios.append(r)
            yield r
        print(num_line, ratios)


def part1(file_path):
    with open(file_path, "r") as f:
        return sum(part_numbers(f))


def part2(file_path):
    with open(file_path, "r") as f:
        return sum(gear_ratios(f))


if __name__ == '__main__':
    res = part2("input.txt")
    print(res)


class Test(TestCase):
    def test_part_number(self):
        lines = """\
......151...88...*.........697.........111-...546*.....663*249...........482*7..........327.......423....513...*........../.880.............
...../.........309........*....-985.........%....................619...=...................*.................335.....808....*............141
........740............414............624..10.720*395........91...../..520......164......318...........397..........*.......560.............\
"""
        [prev, curr, next_line] = lines.splitlines(keepends=True)
        numbers = [n for n in part_number(curr, prev, next_line)]
        self.assertEqual([309, 985, 619, 335, 808], numbers)
