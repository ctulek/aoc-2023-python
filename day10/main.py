def read_data(file_path):
    with open(file_path, 'r') as f:
        data = [list(line) for line in f.read().splitlines()]
    return data


def connections(pipe_type, node):
    x, y = node
    if pipe_type == '|':
        return [(x, y - 1), (x, y + 1)]
    if pipe_type == '-':
        return [(x - 1, y), (x + 1, y)]
    if pipe_type == 'L':
        return [(x + 1, y), (x, y - 1)]
    if pipe_type == 'J':
        return [(x - 1, y), (x, y - 1)]
    if pipe_type == '7':
        return [(x - 1, y), (x, y + 1)]
    if pipe_type == 'F':
        return [(x + 1, y), (x, y + 1)]
    if pipe_type == '.':
        return []


def walk(prev, curr, data):
    pipe_type = data[curr[1]][curr[0]]
    _next = [node for node in connections(pipe_type, curr) if node != prev]
    if len(_next) == 2:
        return None  # Invalid prev, it shouldn't be possible to come to curr from prev with this pipe_type
    _next = _next[0] if _next else None
    if _next is None:
        return None
    x, y = _next
    m, n = len(data), len(data[0])
    if not (0 <= y < m and 0 <= x < n):
        return None
    return _next


def can_walk(prev, curr, data):
    pipe_type = data[curr[1]][curr[0]]
    _next = [node for node in connections(pipe_type, curr) if node != prev]
    return len(_next) == 1


def get_walkers(s_node, data):
    x, y = s_node
    walkers = []
    for ax, ay in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not (0 <= ay < len(data) and 0 <= ax < len(data[0])):
            continue
        if can_walk(s_node, (ax, ay), data):
            walkers.append((s_node, (ax, ay), 1))  # forth parameter is the history of the walker
    return walkers


def find_s_node(data):
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y


def get_meeting_walkers(walkers):
    for i, walker in enumerate(walkers):
        for j, other_walker in enumerate(walkers):
            if i == j:
                continue
            if walker[1] == other_walker[1]:
                return walker, other_walker
    return None


def part1(file_path):
    data = read_data(file_path)
    # for line in data:
    #     print(line)
    s_node = find_s_node(data)
    walkers = get_walkers(s_node, data)
    while walkers:
        new_walkers = []
        for walker in walkers:
            prev, curr, steps = walker
            _next = walk(prev, curr, data)
            if _next is not None:
                new_walkers.append((curr, _next, steps + 1))
        walkers = new_walkers
        meeting_walkers = get_meeting_walkers(walkers)
        if meeting_walkers:
            print(meeting_walkers)
            return meeting_walkers[0][2]
    return walkers


def get_loop_nodes(data):
    s_node = find_s_node(data)
    walkers = [(*walker, [s_node]) for walker in get_walkers(s_node, data)]
    while walkers:
        new_walkers = []
        for walker in walkers:
            prev, curr, steps, history = walker
            _next = walk(prev, curr, data)
            if _next is not None:
                new_walkers.append((curr, _next, steps + 1, history + [curr]))
        walkers = new_walkers
        meeting_walkers = get_meeting_walkers(walkers)
        if meeting_walkers:
            return set([meeting_walkers[0][1]] + meeting_walkers[0][3] + meeting_walkers[1][3])
    return None


# Used Jordan curve theorem to solve this problem
# https://en.wikipedia.org/wiki/Jordan_curve_theorem
# However, it is tricky with the pipes that are not straight lines.
# Combinations:
# 1. I
# 2. F-*J (* means zero or more number of -)
# 3. L-*7
def is_inner_node(node, data):
    x, y = node
    line_count = 0
    i = 0
    while i < x:
        c = data[y][i]
        j = i + 1
        next_c = data[y][j]
        j = j + 1
        while next_c == '-' and j < x:
            next_c = data[y][j]
            j += 1

        if c == '|':
            line_count += 1
        elif c == 'L' and next_c == '7':
            line_count += 1
        elif c == 'F' and next_c == 'J':
            line_count += 1

        i = i + 1

    return line_count % 2 == 1


def part2(file_path):
    data = read_data(file_path)
    loop = get_loop_nodes(data)
    # print(loop)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '.' and (x, y) not in loop:
                data[y][x] = '.'

    ans = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '.':
                if is_inner_node((x, y), data):
                    data[y][x] = 'I'
                    ans += 1
                else:
                    data[y][x] = 'O'

    # for line in data:
    #     print(''.join(line))

    return ans


if __name__ == '__main__':
    res = part1('input.txt')
    print(res)
