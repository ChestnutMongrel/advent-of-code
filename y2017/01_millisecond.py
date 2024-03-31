from common import get_data, timer
from itertools import pairwise


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    check = (
        ('1122', 3),
        ('1111', 4),
        ('1234', 0),
        ('91212129', 9)
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    check = (
        ('1212', 6),
        ('1221', 0),
        ('123425', 4),
        ('123123', 12),
        ('12131415', 4)
    )
    for data, correct in check:
        result = part_two(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


@timer
def part_one(data: str) -> int:
    total = 0
    for first, second in pairwise(data):
        if first == second:
            total += int(first)
    if data[0] == data[-1]:
        total += int(data[0])
    return total


@timer
def part_two(data: str) -> int:
    total = 0
    half = len(data) // 2
    for i, symbol in enumerate(data[half:]):
        if symbol == data[i]:
            total += int(symbol)
    total *= 2
    return total


def main() -> None:
    data = get_data(2017, 1)[0]
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
