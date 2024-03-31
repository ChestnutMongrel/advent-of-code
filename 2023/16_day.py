"""
--- Day 16: The Floor Will Be Lava ---
It works but slowly...
"""


from common import read_file, sum_tuple


def len_path(data: dict) -> int:
    return len(sum_set(data))


def sum_set(data: dict) -> set:
    complete = set()
    for item in data.values():
        complete = complete.union(item)
    return complete


def print_path(field: tuple, path: dict) -> int:
    complete = sum_set(path)

    for i in range(len(field)):
        for ii in range(len(field[i])):
            if (i, ii) in complete:
                print('\033[33m', end='')
            else:
                print('\033[0m', end='')
            print(field[i][ii], end='')
        print()

    return None


def moving_beam(field: tuple, path: dict = None, current: tuple = (0, 0), direction: tuple = (0, 1)) -> dict:

    if not path:
        path = dict()

    n = len(field)
    m = len(field[0])

    while 0 <= current[0] < n and 0 <= current[1] < m:

        symbol = field[current[0]][current[1]]

        x, y = direction
        key = x * 10 + y
        path[key] = path.setdefault(key, set())
        if current in path[key]:
            return path

        path[key].add(current)

        split_beam = (symbol == '|' and x == 0) or (symbol == '-' and y == 0)
        if symbol == '/' or split_beam:
            direction = (y * -1, x * -1)

            if split_beam:
                new_current = sum_tuple(current, direction)
                path.update(moving_beam(field, path, new_current, direction))

        if symbol == '\\' or split_beam:
            direction = y, x

        current = sum_tuple(current, direction)

    return path


def main() -> None:
    name = 'data/16_input.txt'
    data = tuple(read_file(name))

    all_paths_len = set()
    n = len(data)
    m = len(data[0])
    for i in range(n):
        path = moving_beam(data, current=(i, 0))
        all_paths_len.add(len_path(path))
        path = moving_beam(data, current=(i, m-1), direction=(0, -1))
        all_paths_len.add(len_path(path))

    for i in range(m):
        path = moving_beam(data, current=(0, i), direction=(1, 0))
        all_paths_len.add(len_path(path))
        path = moving_beam(data, current=(n-1, i), direction=(-1, 0))
        all_paths_len.add(len_path(path))

    print(max(all_paths_len))


if __name__ == '__main__':
    main()
