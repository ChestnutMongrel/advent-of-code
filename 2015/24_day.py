from common import get_data
from itertools import combinations
from math import prod


def test_all() -> None:
    data = (*range(1, 6), *range(7, 12))
    result = part_one(data, 3)
    correct = 99
    assert correct == result, f'Should be {correct}, got {result} instead.'
    result = part_one(data, 4)
    correct = 44
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: tuple, groups_amount: int) -> int | None:
    group_weight = sum(data) // groups_amount

    for i in range(len(data)):
        qe = set()
        for numbers in combinations(data, i):
            if sum(numbers) == group_weight:
                qe.add(prod(numbers))
        if qe:
            return min(qe)

    return None


def main() -> None:
    data = tuple(map(int, get_data(2015, 24)))
    print('Part one:', part_one(data, 3))
    print('Part two:', part_one(data, 4))


if __name__ == '__main__':
    test_all()
    main()
