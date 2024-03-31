from common import read_file, get_data
from collections import defaultdict

YEAR = 2017
DAY = 24


def test_all() -> None:
    data = parse_data(read_file('data/24_example.txt'))
    # print(data)
    result = part_one(data)
    correct = 31
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'
    # check = ()
    # for data, correct in check:
    #     result = part_one(data)
    #     assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple[str]) -> dict:
    result = defaultdict(set)
    for line in data:
        start, end = map(int, line.split('/'))
        result[start].add(end)
        result[end].add(start)
    return dict(result)


def part_one(data: dict[int: list]) -> int:
    # loops = set()
    # for point in data:
    #     if point in data[point]:
    #         loops.add(point)
    #         data[point].remove(point)
    # print(f'{loops = }')

    # Will it be faster with not a full bridge, but with a start, an end, and every part?

    completed_bridges = list()
    start = 0
    bridges = [((start, item),) for item in data[start]]

    while True:
        new_bridges = list()

        for current in bridges:
            last = current[-1][-1]
            for point in data[last]:
                if (last, point) not in current and \
                        (point, last) not in current:
                    new_bridges.append(current + ((last, point),))
            if current not in completed_bridges:
                completed_bridges.append(current)
                # print(current)
        if not new_bridges:
            break
        print(len(new_bridges))
        bridges = new_bridges

    max_weight = 0
    for path in completed_bridges:
        weight = sum(x + y for x, y in path)
        if weight > max_weight:
            max_weight = weight

    return max_weight


def main() -> None:
    data = parse_data(get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(data))
    # 1235 is too low
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
