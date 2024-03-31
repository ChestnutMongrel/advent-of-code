from common import read_file, get_data, sum_tuple
from y2017.ten_millisecond import knot_hashing


YEAR = 2017
DAY = 14


def test_all() -> None:
    key = 'flqrgnkx'
    grid = make_grid(key)

    check = (
        (part_one(grid), 8108),
        (part_two(tuple(read_file('data/14_example.txt'))), 9),
        (part_two(grid), 1242),

    )
    for result, correct in check:
        assert correct == result, f'For {key} should be {correct}, got {result} instead.'


def convert_to_binary(hex_number: str) -> str:
    size = 128
    number = int(hex_number, 16)
    return f'{number:0>{size}b}'


def make_grid(key: str) -> tuple:
    size = 128
    grid = list()
    for i in range(size):
        hex_line = knot_hashing(f'{key}-{i}')
        binary_line = convert_to_binary(hex_line)
        grid.append(binary_line)
    return tuple(grid)


def get_neighbors(current: tuple) -> tuple:
    neighbors = (
        (0, 1), (0, -1),
        (1, 0), (-1, 0),
    )
    for shift in neighbors:
        yield sum_tuple(current, shift)


def part_one(grid: tuple) -> int:
    total = 0
    for line in grid:  # type: str
        total += line.count('1')
    return total


def part_two(grid: tuple) -> int:
    size = len(grid)
    visited = [[0] * size for _ in range(size)]
    groups = 0
    for x in range(size):
        for y in range(size):
            if grid[x][y] == '0':
                visited[x][y] = 1
            elif not visited[x][y]:
                groups += 1
                members = {(x, y)}
                while members:
                    current = temp_x, temp_y = members.pop()
                    if grid[temp_x][temp_y] != '0':
                        visited[temp_x][temp_y] = 1
                        for i, ii in get_neighbors(current):
                            if 0 <= i < size and 0 <= ii < size \
                                    and not visited[i][ii]:
                                members.add((i, ii))

    return groups


def main() -> None:
    data = get_data(year=YEAR, day=DAY)[0]
    grid = make_grid(data)
    print('Part one:', part_one(grid))
    print('Part two:', part_two(grid))


if __name__ == '__main__':
    test_all()
    main()
