from common import read_file, get_data, sum_tuple
from dataclasses import dataclass
import re
from itertools import permutations


# I probably don't need a dataclass, but it's 0:55, I can't think anything better...
# @dataclass
# class Node:
#     name: tuple
#     used: int
#     avail: int


def test_all() -> None:
    data = parse_data(read_file('data/22_example.txt'))
    # for key, values in data.items():
    #     print(key, values)

    print(simplify_data(data))
    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> dict:
    # The data titles is:
    # "Filesystem              Size  Used  Avail  Use%"

    result = dict()
    name_pattern = re.compile(r'node-x(\d+)-y(\d+)')

    for line in data:  # type: str
        if found := name_pattern.search(line):
            x, y = map(int, found.groups(line))
            info = line.split()
            used = int(info[2][:-1])
            avail = int(info[3][:-1])
            result[(x, y)] = {'used': used, 'avail': avail}

    return result


def simplify_data(data: dict) -> tuple | None:
    # The first one will be empty.
    neighbors = (
        (0, 1), (0, -1), (1, 0), (-1, 0)
    )
    empty = None
    can_be_moved = list()
    for key, value in data.items():
        # print(key, value)
        for move in neighbors:
            neighbor = sum_tuple(key, move)
            if neighbor in data and value['used'] > sum(data[neighbor].values()):
                # print('skipping', key)
                # print()
                break
        else:
            if value['used'] == 0:
                if empty:
                    return None
                else:
                    empty = key
            else:
                can_be_moved.append(key)

    result = (empty,) + tuple(can_be_moved)
    max_used = max(data[key]['used'] for key in result)
    min_size = min(sum(data[key].values()) for key in result)

    if max_used > min_size:
        return None
    return result


def part_one(data: dict) -> int:
    total = 0

    for first, second in permutations(data.values(), 2):
        if first['used'] and first['used'] <= second['avail']:
            total += 1

    return total


def calm_down(data: dict) -> int:
    total = 0

    for first, second in permutations(data.keys(), 2):
        if (first[0] == second[0] and abs(first[1] - second[1]) == 1) or \
                (first[1] == second[1] and abs(first[0] - second[0]) == 1):
            if data[first]['used'] <= data[second]['avail']:
                total += 1

    return total


def count_shortest_path(data: tuple, start: tuple, finish: tuple) -> int:
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    pass


def part_two(data: tuple) -> int:
    x_max = max((item[0] for item in data))
    y_max = max((item[1] for item in data))
    goal = (x_max, 0)
    access = (0, 0)
    empty = data[0]

    print(empty)

    # Find the ways from the empty spot to the left and to the down from the goal. -- 69 --
    # Find the ways from previous spots to the access spot. -- 28 --
    # Find ways to move the empty spot from behind the goal to in front of the goal.

    steps = 1
    while steps:
        break
        # if goal == access:
        #     return steps

    print(goal)


def print_grid(data: tuple[tuple]) -> None:
    x_max = max((item[0] for item in data))
    y_max = max((item[1] for item in data))
    goal = (x_max, 0)
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if (x, y) == data[0]:
                print('- ', end='')
            elif (x, y) == goal:
                print('G ', end='')
            elif (x, y) in data:
                print('. ', end='')
            else:
                print('# ', end='')
        print()


def main() -> None:
    data = get_data(2016, 22)
    data = parse_data(data)
    print('Part one:', part_one(data))
    print('Only neighbors:', calm_down(data))
    simple_data = simplify_data(data)
    print_grid(simple_data)

    # print('Part two:', part_two(data))
    # 157 is too low
    # 230 is too high


if __name__ == '__main__':
    test_all()
    main()
