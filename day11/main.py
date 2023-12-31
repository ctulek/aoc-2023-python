def read_data(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f.readlines()]


def get_galaxies(universe):
    return [(r, c) for r in range(len(universe)) for c in range(len(universe[0])) if universe[r][c] == '#']


def expand_universe(universe, expand):
    m, n = len(universe), len(universe[0])
    empty_rows = [True] * m
    empty_cols = [True] * n
    for r in range(m):
        for c in range(n):
            if universe[r][c] == '#':
                empty_rows[r] = False
                empty_cols[c] = False
            else:
                universe[r][c] = 1

    for r in range(len(universe)):
        if empty_rows[r]:
            for c in range(len(universe[0])):
                universe[r][c] = expand

    for c in range(len(universe[0])):
        if empty_cols[c]:
            for r in range(len(universe)):
                universe[r][c] = expand

    return universe


# Manhattan distance
def distance(galaxy1, galaxy2, universe):
    r1, c1 = galaxy1
    r2, c2 = galaxy2

    width = 0
    height = 0
    for c in range(min(c1, c2), max(c1, c2)):
        width += universe[0][c] if universe[0][c] != '#' else 1
    for r in range(min(r1, r2), max(r1, r2)):
        height += universe[r][0] if universe[r][0] != '#' else 1

    return width + height


def distances(file_path, expand):
    universe = read_data(file_path)

    galaxies = get_galaxies(universe)
    universe = expand_universe(universe, expand)

    return [distance(galaxies[i], galaxies[j], universe)
            for i in range(len(galaxies))
            for j in range(i + 1, len(galaxies))]


def part1(file_path):
    return sum(distances(file_path, 2))


def part2(file_path):
    return sum(distances(file_path, 1000000))


if __name__ == '__main__':
    res = part2('input.txt')
    print(res)
