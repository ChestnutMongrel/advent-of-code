from common import get_data
from math import ceil

YEAR = 2017
DAY = 6


def test_all() -> None:
    data = tuple(map(int, '0 2 7 0'.split()))
    result = part_one(data)
    correct = (5, 4)
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def reload(data: tuple) -> tuple:
    blocks_amount = len(data)
    new_data = list(data)

    biggest = max(data)
    ind_max = data.index(biggest)

    new_data[ind_max] = 0
    load = ceil(biggest / blocks_amount)
    amount = biggest % blocks_amount or blocks_amount

    for ind in range(ind_max + 1, ind_max + amount + 1):
        new_data[ind % blocks_amount] += load
    load -= 1
    for ind in range(ind_max + amount + 1, ind_max + blocks_amount + 1):
        new_data[ind % blocks_amount] += load

    return tuple(new_data)


def part_one(data: tuple) -> tuple:
    circles = 0
    configurations = set()
    configurations.add(data)

    while True:
        circles += 1

        data = reload(data)
        if data in configurations:
            first_occurrence = circles
            repeated_state = data
            break

        configurations.add(data)

    circles = 0
    while True:
        circles += 1
        data = reload(data)
        if data == repeated_state:
            break

    return first_occurrence, circles


def main() -> None:
    data = tuple(map(int, get_data(year=YEAR, day=DAY)[0].split()))
    result_one, result_two = part_one(data)
    print('Part one:', result_one)
    print('Part two:', result_two)


if __name__ == '__main__':
    test_all()
    main()
