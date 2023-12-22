import math


def read_map(file_path: str):
    with open(file_path, "r") as f:
        data_map = {"seeds": [], "maps": []}
        state = "seeds"
        map_lines = []
        for line in f:
            line = line.strip()
            if state == "seeds":
                seeds = list(map(int, line.split(":")[1].strip().split(" ")))
                data_map["seeds"] = seeds
                state = "maps"
            elif state == "maps":
                if line == "":
                    continue
                elif not line[0].isdigit():
                    if map_lines:
                        data_map["maps"].append(map_lines)
                    map_lines = []
                else:
                    dest, source, _range = list(map(int, line.split(" ")))
                    map_lines.append((dest, source, _range))

        data_map["maps"].append(map_lines)

        return data_map


def find_mapping(value, mappings):
    for dest, source, _range in mappings:
        if source <= value <= (source + _range - 1):
            return dest + (value - source)
    return value


def find_location(seed, data_map):
    curr = seed
    for mapping in data_map["maps"]:
        curr = find_mapping(curr, mapping)
    return curr


def find_mapping_range(start, end, mappings):
    for dest, source, _range in mappings:
        source_end = source + _range - 1
        if source <= start <= source_end:
            dest_start = dest + (start - source)
            if end <= source_end:
                range_end = dest_start + (end - start)
                return dest_start, range_end, None, None
            else:
                range_end = dest_start + (source_end - start)
                return dest_start, range_end, source_end + 1, end
    return start, end, None, None


def get_ranges_for_range(start, end, mappings):
    dest_start, dest_end, start_extra, end_extra = find_mapping_range(start, end, mappings)
    ranges = [(dest_start, dest_end)]
    while start_extra is not None:
        dest_start, dest_end, start_extra, end_extra = find_mapping_range(start_extra, end_extra, mappings)
        ranges.append((dest_start, dest_end))

    return ranges


def min_location_for_ranges(ranges, data_map):
    current_ranges = ranges
    for mappings in data_map["maps"]:
        new_ranges = []
        for start, end in current_ranges:
            new_ranges += get_ranges_for_range(start, end, mappings)
        current_ranges = new_ranges
    return min([start for start, end in current_ranges])


def part1(file_path: str):
    data_map = read_map(file_path)
    ans = math.inf
    for seed in data_map["seeds"]:
        location = find_location(seed, data_map)
        ans = min(ans, location)

    return ans


def part2(file_path: str):
    data_map = read_map(file_path)
    seed_ranges = []
    for i in range(0, len(data_map["seeds"]), 2):
        start, end = data_map["seeds"][i], data_map["seeds"][i] + data_map["seeds"][i + 1] - 1
        seed_ranges.append((start, end))

    return min_location_for_ranges(seed_ranges, data_map)


if __name__ == '__main__':
    res = part2("input.txt")
    print(res)
