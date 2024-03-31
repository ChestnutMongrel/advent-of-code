from common import read_file, get_data, sum_tuple, timer
from copy import deepcopy


def test_all() -> None:
    data = to_matrix(read_file('data/18_example.txt'))

    result = part_one(data, 4)
    correct = 4
    assert correct == result, f'Should be {correct}, got {result} instead.'

    result = part_one(data, 5, True)
    correct = 17
    assert correct == result, f'Should be {correct}, got {result} instead.'


def to_matrix(data: str) -> list:
    return list(list(line) for line in data)


@timer
def part_one(matrix: list, steps: int = 100, always_on: bool = False) -> int:
    neighbors = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )
    size = len(matrix)
    corners = (
        (0, 0), (0, size - 1),
        (size - 1, 0), (size - 1, size - 1)
    )
    if always_on:
        for x, y in corners:
            matrix[x][y] = '#'

    for count in range(steps):
        copy_matrix = deepcopy(matrix)
        for i in range(size):
            for ii in range(size):
                if always_on and (i, ii) in corners:
                    continue
                on_amount = 0
                for coord in neighbors:
                    x, y = sum_tuple(coord, (i, ii))
                    if 0 <= x < size and 0 <= y < size:
                        on_amount += int(matrix[x][y] == '#')
                if matrix[i][ii] == '#' and on_amount not in (2, 3):
                    copy_matrix[i][ii] = '.'
                elif matrix[i][ii] == '.' and on_amount == 3:
                    copy_matrix[i][ii] = '#'
        matrix = copy_matrix

    return sum(line.count('#') for line in matrix)


def main() -> None:
    matrix = to_matrix(get_data(2015, 18))
    print('Part one:', part_one(matrix, 100))
    print('Part two:', part_one(matrix, 100, always_on=True))


if __name__ == '__main__':
    test_all()
    main()
