def read_data(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split(" "))) for line in f.readlines()]


def differences(numbers):
    return [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]


def history_sequences(history):
    sequences = []
    sequence = differences(history)
    while any([s != 0 for s in sequence]):
        sequences.append(sequence)
        sequence = differences(sequence)
    sequences.append(sequence)
    return sequences


def next_value(history):
    sequences = history_sequences(history)
    return sum([s[-1] for s in sequences]) + history[-1]


def prev_value(history):
    sequences = history_sequences(history)
    curr = sequences[-1][0]
    for sequence in reversed(sequences[:-1]):
        curr = sequence[0] - curr
    return history[0] - curr


def part1(file_path):
    histories = read_data(file_path)
    return sum([next_value(history) for history in histories])


def part2(file_path):
    histories = read_data(file_path)
    return sum([prev_value(history) for history in histories])


if __name__ == '__main__':
    res = part2('input.txt')
    print(res)
