from common import read_file, get_data
import re
import json


def test_all() -> None:
    check = (
        ('[1,2,3]', 6),
        ('{"a":2,"b":4}', 6),
        ('[[[3]]]', 3),
        ('{"a":{"b":4},"c":-1}', 3),
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'

    check = (
        ('[1,2,3]', 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    )
    for data, correct in check:
        result = part_two(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(line: str) -> int:
    pattern = r'"{0}-?\d+"{0}'
    numbers = map(int, re.findall(pattern, line))
    return sum(numbers)


def get_num(data) -> int:
    if type(data) is int:
        return data

    if type(data) is str:
        return 0

    if type(data) is list:
        return sum(map(get_num, data))

    if type(data) is dict:
        if 'red' in data.values():
            return 0
        return sum(map(get_num, data.values()))


def part_two(line: str) -> int:
    json_dict = json.loads(line)
    return get_num(json_dict)


def main() -> None:
    line = tuple(get_data(2015, 12))[0]
    print('Part one:', part_one(line))
    print('Part two:', part_two(line))


if __name__ == '__main__':
    test_all()
    main()
