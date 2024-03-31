from common import read_file, get_data
from collections import namedtuple


YEAR = 2017
DAY = 7
Info = namedtuple('Info', ['weight', 'carry'])


def test_all() -> None:
    data = tuple(read_file('data/07_example.txt'))
    parsed = parse_data(data)

    result = part_one(parsed)
    correct = 'tknk'
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'
    count_weight(parsed, 'tknk')


def part_one(data: dict) -> str:
    carried = set(data.keys())
    for _, carry in data.values():
        if carry:
            carried -= set(carry)
    return carried.pop()


def parse_data(data: tuple[str]) -> dict:
    # The line in data looks like this:
    # fwft (72) -> ktlj, cntj, xhth

    parsed = dict()
    for line in data:
        if '->' in line:
            line, names = line.split(' -> ')
            names = names.split(', ')
        else:
            names = list()
        name, weight = line[:-1].split(' (')
        info = Info(weight=int(weight), carry=names)
        parsed[name] = info

    return parsed


# This is a cheating, need to rewrite!
def count_weight(data: dict[str: Info], start: str) -> int:
    if not data[start].carry:
        return data[start].weight

    weights = [count_weight(data, name) for name in data[start].carry]
    if max(weights) == min(weights):
        return sum(weights) + data[start].weight

    print(weights)
    print([data[name].weight for name in data[start].carry])
    return sum(weights) + data[start].weight


def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    parsed = parse_data(data)
    bottom = part_one(parsed)
    print('Part one:', bottom)
    count_weight(parsed, bottom)
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
