from common import get_data


def test_all() -> None:
    data = '''5-8
0-2
4-7'''
    parsed_data = parse_data(data.split('\n'))
    result = part_one(parsed_data)
    correct = 3
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'
    result = part_two(parsed_data, 9)
    correct = 2
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> tuple:
    result = list()
    for line in data:
        result.append(tuple(map(int, line.split('-'))))
    return tuple(result)


def combine(first: tuple, second: tuple) -> tuple:
    if first[0] > second[0]:
        first, second = second, first

    if second[0] - first[1] > 1 or first[1] >= second[1]:
        return first
    else:
        return first[0], second[1]


def part_one(ranges: tuple) -> int:
    sorted_data = sorted(ranges, key=lambda x: x[0])
    current = sorted_data[0]
    for item in sorted_data:
        current = combine(current, item)
        if current[1] < item[0]:
            return current[1] + 1
    return -1


def part_two(ranges: tuple, highest: int) -> int:
    sorted_data = sorted(ranges, key=lambda x: x[0])
    current = sorted_data[0]
    total = 0
    for item in sorted_data:
        current = combine(current, item)
        if current[1] < item[1]:
            total += item[0] - current[1] - 1
            current = item
    total += highest - current[1]
    return total


def main() -> None:
    data = get_data(2016, 20)
    data = parse_data(data)
    highest = 4294967295
    print('Part one:', part_one(data))
    print('Part two:', part_two(data, highest))


if __name__ == '__main__':
    test_all()
    main()
