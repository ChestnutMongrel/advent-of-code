from common import read_file, get_data, sum_tuple
import re
from itertools import combinations, permutations, pairwise


def test_all() -> None:
    data = tuple(read_file('data/24_example.txt'))
    results = part_one(data)
    correct = (14, 20)

    for result, should_be in zip(results, correct):
        assert should_be == result, f'Should be {should_be}, got {result} instead.'


def shortest_path(maze: tuple, start: tuple, finish: tuple) -> int:
    steps = 0
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = [start]
    to_go = (start,)

    while True:
        if not to_go:
            return 0
        steps += 1
        new_to_go = list()
        for current in to_go:
            for shift in moves:
                new_current = x, y = sum_tuple(current, shift)
                if maze[x][y] != '#' and new_current not in visited:
                    if new_current == finish:
                        return steps
                    visited.append(new_current)
                    new_to_go.append(new_current)
        to_go = tuple(new_to_go)


# What took you so long?..
def part_one(data: tuple) -> tuple:
    points = find_numbers(data)

    paths = dict()
    for first, second in combinations(points, 2):
        paths[first, second] = shortest_path(data, points[first], points[second])

    shortest = shortest_with_return = float('inf')
    start = 0
    numbers = tuple((item for item in points if item != start))
    for path in permutations(numbers, len(numbers)):
        length = 0
        path = (start,) + path
        for first, second in pairwise(path):
            length += paths.get((first, second), paths.get((second, first)))
        if length < shortest:
            shortest = length
        length += paths.get((path[-1], start), paths.get((start, path[-1])))
        if length < shortest_with_return:
            shortest_with_return = length

    return shortest, shortest_with_return


def find_numbers(maze: tuple) -> dict:
    numbers = dict()
    pattern = re.compile(r'\d')

    for i, line in enumerate(maze):
        if found := pattern.findall(line):
            for symbol in found:
                ind = line.index(symbol)
                numbers[int(symbol)] = (i, ind)

    return numbers


def main() -> None:
    data = get_data(2016, 24)
    result, result_with_return = part_one(data)
    print('Part one:', result)
    print('Part two:', result_with_return)


if __name__ == '__main__':
    test_all()
    main()
