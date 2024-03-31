from common import read_file, get_data

YEAR = 2017
DAY = 12


def test_all() -> None:
    data = parse_data(read_file('data/12_example.txt'))
    check = (
        (part_one(data), 6),
        (part_two(data), 2)
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> dict:
    # A line of the data looks like this:
    # 2 <-> 0, 3, 4

    connections = dict()
    for line in data:  # type: str
        key, values = line.split(' <-> ')
        connections[key] = values.split(', ')
    return connections


def part_one(data: dict) -> int:
    return len(find_group(data, '0'))


def part_two(data: dict) -> int:
    groups_amount = 0
    visited = set()

    for key in data:
        if key not in visited:
            group = find_group(data, key)
            visited.update(group)
            groups_amount += 1

    return groups_amount


def find_group(data: dict, start: str) -> set:
    connected = {start}
    checked = set()

    while checked != connected:
        new_to_add = list()
        for value in connected:
            new_to_add += data[value]
            checked.add(value)
        connected.update(new_to_add)
    return connected


def main() -> None:
    data = parse_data(get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
