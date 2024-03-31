"""
--- Day 10: Pipe Maze ---
"""


def read_file(file_name: str) -> str:
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip()


def find_start(maze: list) -> tuple:
    for line in maze:
        x = line.find('S')
        if x != -1:
            y = maze.index(line)
            break
    return y, x


def where_to_go_from(start: tuple, symbol: str) -> tuple:
    # In the map first number is for vertical, second is for horizontal.

    map_ = {
        '|': ((-1, 0), (1, 0)),
        '-': ((0, -1), (0, 1)),
        'L': ((-1, 0), (0, 1)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, -1), (1, 0)),
        'F': ((1, 0), (0, 1)),
        '.': ((0, 0), (0, 0)),
        'S': ((0, 0), (0, 0))
    }

    first, second = map_[symbol]
    return sum_tuple(first, start), sum_tuple(second, start)


def start_symbol(start: tuple, maze: list) -> str:
    to_go = set()

    for diffs in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        current = x, y = sum_tuple(start, diffs)
        if start in tuple(where_to_go_from(current, maze[x][y])):
            to_go.add(diffs)

    for i in '|-LJ7F':
        if set(where_to_go_from((0, 0), i)) == to_go:
            return i


def sum_tuple(a: tuple, b: tuple) -> tuple:
    return a[0] + b[0], a[1] + b[1]


def find_path(maze: list) -> list:
    start = x, y = find_start(maze)
    path = list()
    new_line = maze[x].replace('S', start_symbol(start, maze))
    maze.pop(x)
    maze.insert(x, new_line)

    current = where_to_go_from(start, maze[x][y])[0]
    path.append(current)
    prev = start
    while current != start:
        x, y = current
        for var in where_to_go_from(current, maze[x][y]):
            if var != prev:
                prev = current
                current = var
                path.append(current)
                break

    return path


def make_maze(file_name: str) -> list:
    maze = list()
    for line in read_file(file_name):
        maze.append('.' + line + '.')
    maze.append('.' * len(maze[0]))
    maze.insert(0, maze[-1])
    return maze


def count_inside(maze: list, path: list) -> int:
    total = 0
    switch = ({'L', '7'}, {'F', 'J'})

    for x in range(1, len(maze) - 1):
        outside = True
        prev_node = ''
        for y in range(1, len(maze[0]) - 1):
            if (x, y) in path:
                symbol = maze[x][y]
                if symbol == '|':
                    outside = not outside
                elif symbol == '-':
                    continue
                elif not prev_node:
                    prev_node = symbol
                else:
                    if set((prev_node, symbol)) in switch:
                        outside = not outside
                    prev_node = ''
            elif not outside:
                total += 1
    return total


def main() -> None:

    for name in ('data/10_input.txt',):  # 'data/12_example.txt', 'data/example_12.txt',
        maze = make_maze(name)
        path = find_path(maze)
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if (x, y) == path[-1]:
                    print('\033[31m', end='')
                elif (x, y) in path:
                    print('\033[32m', end='')
                else:
                    print('\033[0m', end='')
                print(maze[x][y], end='')
            print()
        print('Steps to farthest point:', len(path) // 2)
        print('Enclosed tiles:', count_inside(maze, path))


if __name__ == '__main__':
    main()