import operator
from functools import reduce


def read_data(file_path):
    with open(file_path, "r") as f:
        times, records = f.readlines()
        times = filter(lambda x: bool(x), times.strip().split(" ")[1:])
        records = filter(lambda x: bool(x), records.strip().split(" ")[1:])
    return zip(map(int, times), map(int, records))


def combinations(time, record):
    ans = 0
    for speed in range(1, time):
        if speed * (time - speed) > record:
            ans += 1
    return ans


def list_combinations(data):
    for time, record in data:
        yield combinations(time, record)


def part1(file_path):
    data = read_data(file_path)
    return reduce(operator.mul, list_combinations(data), 1)


if __name__ == '__main__':
    res = part1("part2_input.txt")
    print(res)
