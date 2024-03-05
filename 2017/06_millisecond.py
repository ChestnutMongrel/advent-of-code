from common import read_file, get_data
from math import ceil

YEAR = 2017
DAY = 6


def test_all() -> None:
    data = tuple(map(int, '0 2 7 0'.split()))
    result = part_one(data)
    correct = 5
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def reload(data: tuple) -> tuple:
    pass


def part_one(data: tuple) -> int:
    circles = 0
    blocks_amount = len(data)
    configurations = set()
    configurations.add(data)
    first_occurrence = None
    repeated_state = None

    while True:
        circles += 1
        new_data = list(data)

        biggest = max(data)
        ind_max = data.index(biggest)

        new_data[ind_max] = 0
        load = ceil(biggest / blocks_amount)
        amount = biggest % blocks_amount or blocks_amount
        rest = blocks_amount - amount

        # data = [data[(ind_max + i) % blocks_amount] \
        #         for i in range(blocks_amount) if ]

        for ind in range(ind_max + 1, ind_max + amount + 1):
            new_data[ind % blocks_amount] += load
        load -= 1
        for ind in range(ind_max + amount + 1, ind_max + blocks_amount + 1):
            new_data[ind % blocks_amount] += load

        data = tuple(new_data)
        if data in configurations:
            break

        configurations.add(data)
        print(data)

    return circles


def main() -> None:
    data = tuple(map(int, get_data(year=YEAR, day=DAY)[0].split()))
    print('Puzzle input:', data)
    print('Part one:', part_one(data))
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
