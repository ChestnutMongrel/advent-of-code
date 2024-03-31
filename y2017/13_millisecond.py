from common import read_file, get_data

YEAR = 2017
DAY = 13


def test_all() -> None:
    data = parse_data(read_file('data/13_example.txt'))
    check = (
        (part_one(data), 24),
        (part_two(data), 10),
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> dict:
    result = dict()
    for line in data:
        depth, size = map(int, line.split(': '))
        result[depth] = size
    return result


def part_one(data: dict) -> int:
    severity = 0
    for position, size in data.items():
        if position % ((size - 1) * 2) == 0:
            severity += position * size

    return severity


# It probably could be done faster...
def part_two(data: dict) -> int:
    delay = 0
    while True:
        for position, size in data.items():
            if (position + delay) % ((size - 1) * 2) == 0:
                break
        else:
            return delay
        delay += 1


def main() -> None:
    data = parse_data(get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
