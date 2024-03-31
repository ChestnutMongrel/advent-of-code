from common import read_file, get_data
from itertools import combinations


def test_all() -> None:
    containers = (20, 15, 10, 5, 5)
    to_store = 25
    correct = 4
    result = part_one(to_store, containers)
    # for data, correct in check:
    #     result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'

    correct_min = 3
    result_min = part_one(to_store, containers, True)
    assert correct_min == result_min, f'Should be {correct_min}, got {result_min} instead.'


def part_one(to_store: int, containers: tuple, find_minimum: bool = False) -> int:
    fit = 0
    for i in range(1, len(containers)):
        # print(*combinations(containers, i))
        for variation in combinations(containers, i):
            if sum(variation) == to_store:
                fit += 1
        if fit and find_minimum:
            return fit
    return fit


def main() -> None:
    data = tuple(map(int, get_data(2015, 17)))
    to_store = 150
    print('Part one:', part_one(to_store, data))
    print('Part two:', part_one(to_store, data, True))
    # print('Part two:', result)


if __name__ == '__main__':
    test_all()
    main()
