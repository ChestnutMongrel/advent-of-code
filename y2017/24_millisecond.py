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
    return result


def part_one(data: dict[int: list]) -> int:
    loops = set()
    for point in data:
        if point in data[point]:
            loops.add(point)
            data[point].remove(point)
    # print(f'{loops = }')

    completed_bridges = list()
    bridges = [(0,)]
    while True:
        new_bridges = list()
        for current in bridges:
            last = current[-1]
            for point in data[last]:
                if point not in current:
                    new_bridges.append(current + (point,))
                elif point != current[-2]:
                    completed_bridges.append(current + (point,))
            if current not in completed_bridges:
                completed_bridges.append(current)
        if not new_bridges:
            break
        bridges = new_bridges

    max_weight = 0
    for path in completed_bridges:
        print(f'{path = }')
        weight = sum(path) * 2 - path[0] - path[-1] + sum(loops.intersection(path)) * 2
        print(f'{weight = }')
        if weight > max_weight:
            max_weight = weight

    return max_weight


def main() -> None:
    data = parse_data(get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(data))
    # 1235 is loo low
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
