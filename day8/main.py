from math import lcm


def read_data(file_path):
    with open(file_path, 'r') as f:
        lr_instructions = None
        node_lines = []
        for line in f:
            if not lr_instructions:
                lr_instructions = line.strip()
            elif line.strip() == '':
                continue
            else:
                node_name, children = line.strip().split('=')
                node_name = node_name.strip()
                children = children.replace('(', '').replace(')', '').strip()
                children = children.split(', ')
                node_lines.append((node_name, children))

        return lr_instructions, node_lines


def nodes_dict(node_lines):
    nodes = {}
    for node_name, children in node_lines:
        nodes[node_name] = children

    return nodes


def part1(file_path):
    lr_instructions, node_lines = read_data(file_path)
    nodes = nodes_dict(node_lines)
    ans = 0
    curr_node = 'AAA'
    pos = 0
    while curr_node != 'ZZZ':
        curr_direction = lr_instructions[pos]
        if curr_direction == 'L':
            curr_node = nodes[curr_node][0]
        elif curr_direction == 'R':
            curr_node = nodes[curr_node][1]

        pos += 1
        pos = pos % len(lr_instructions)
        ans += 1

    return ans


def get_periods(start, nodes, instructions):
    periods = []

    first_z = None
    curr_node = start
    pos = 0
    steps = 0
    while True:
        curr_node = nodes[curr_node][0] if instructions[pos] == 'L' else nodes[curr_node][1]
        pos += 1
        pos %= len(instructions)
        steps += 1
        if curr_node.endswith('Z'):
            periods.append(steps)
            steps = 0
            if not first_z:
                first_z = curr_node
            elif first_z == curr_node:
                break

    return periods


# Part 2 solution inspired from: https://youtu.be/_nnxLcrwO_U?t=316
def part2(file_path):
    lr_instructions, node_lines = read_data(file_path)
    nodes = nodes_dict(node_lines)
    start_nodes = [node[0] for node in node_lines if node[0][2] == 'A']
    periods = [get_periods(start, nodes, lr_instructions) for start in start_nodes]
    # If you print periods, you will see they are all the length of two and the first and last elements are the same
    # print(periods)
    numbers = [periods[0] for periods in periods]
    # And the numbers are all divisible by len(lr_instructions)
    # print([n % len(lr_instructions) for n in numbers])
    ans = lcm(*numbers)

    return ans


if __name__ == '__main__':
    res = part2("input.txt")
    print(res)
