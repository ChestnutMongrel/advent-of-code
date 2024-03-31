from common import read_file, sum_tuple


count = 0


def one_line(field: tuple, begin: tuple, current: tuple) -> tuple:
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    path = list()
    path.append(begin)

    while True:
        new_cells = list()
        path.append(current)
        for item in moves:
            x, y = sum_tuple(current, item)
            if x and y and (x, y) not in path and field[x][y] != '#':
                new_cells.append((x, y))

        if len(new_cells) != 1:
            return tuple(path), new_cells
        current = new_cells[0]


def find_lines(field: tuple, start: tuple, finish: tuple) -> dict:

    lines = dict()

    # moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    to_go = {start: (start,)}

    # prev = -1, start[1]
    # first = list()
    # first.append(start)
    # print(first)
    visited = set()

    while to_go:
        new_to_go = dict()
        for begin, values in to_go.items():
            for current in values:
                line, next_moves = one_line(field, begin, current)
                # If line reached a dead end (which can be only if there are a finish or slopes there).
                if not next_moves:
                    if line[-1] != finish:
                        continue
                # if line[-1] in visited:
                #     continue
                if begin not in lines:
                    lines[begin] = list()
                if line not in lines[begin]:
                    lines[begin].append(line)
                visited.update(line)
                if line[-1] not in lines:
                    # for item in next_moves:
                    #     if item in visited:
                    #         next_moves.remove(item)
                    if next_moves:
                        new_to_go[line[-1]] = next_moves

        # print(f'{new_to_go = }')
        to_go = new_to_go
        # break

    return lines

    # longest = list(lines[start][0][2:])
    # print(f'{longest = }')
    # keep_going = lines[start][0][-1] != finish
    # change = True
    #
    # while change and (last := longest[-1]) != finish:
    #     print(f'{last = }')
    #     change = False
    #     if last in lines:
    #         for item in sorted(lines[last], reverse=True, key=len):
    #             if item[-1] not in longest:
    #                 longest.extend(item)
    #                 change = True
    #                 break


def count_longest_path(lines: dict, start: tuple, finish: tuple) -> int:
    longest = [list(lines[start][0][2:])]

    # Print only start, finish, and length.
    for key, values in lines.items():
        print(key)
        for item in values:
            print('\t', item[0], '-', len(item) - 1, '-', item[-1])
        print()

    return 0
    keep_going = lines[start][0][-1] != finish

    while keep_going:
        new_longest = list()
        while longest:
            line = longest.pop()
            last = line[-1]
            if last in lines:  # or last == finish:
                for value in lines[last]:
                    if value[-1] not in line:
                        new_longest.append(list(line) + list(value[1:]))
            elif last == finish:
                new_longest.append(line)
                print('with finish', len(line))
        longest = new_longest
        print(len(longest))
        keep_going = any(item[-1] != finish for item in longest)

    print('max')
    print(len(max(longest, key=len)))


def all_paths(field: tuple) -> int:
    paths = list()
    start = 1, field[1].find('.')
    finish = len(field) - 2, field[-2].rfind('.')
    visited = set()

    def path(current: tuple, steps: set) -> None:
        moves = {
            '>': (0, 1),
            '<': (0, -1),
            '^': (-1, 0),
            'v': (1, 0)
        }
        # print(paths)
        prev = -1, current[1]
        while current != finish:
            visited.add(current)
            # print(count)
            # print(f'{current = }')
            # prev = current
            steps.add(current)

            x, y = current
            symbol = field[x][y]

            if symbol in moves:
                x, y = sum_tuple(current, moves[symbol])
                if (x, y) == prev or (x, y) in steps:
                    return
                prev = current
                current = x, y

            else:  # symbol == '.'
                to_go = list()
                # print(f'{symbol = }')
                # print(steps)
                for move in moves.values():
                    x, y = sum_tuple(current, move)
                    # print(f'{prev = }')
                    if x and y and (x, y) != prev and field[x][y] != '#' and (x, y) not in visited:
                        # print(x, y)
                        to_go.append((x, y))
                for move in to_go[:-1]:
                    # print(move)
                    path(move, steps.copy())
                prev = current
                # print(f'{to_go = }')
                if to_go:
                    current = to_go[-1]
                else:
                    return

        else:
            paths.append(steps)
            return

    path(start, set())
    print('result')
    print([len(item) for item in paths])
    print(max(paths, key=len))


def start_finish(field: tuple) -> tuple:
    start = 1, field[1].find('.')
    finish = len(field) - 2, field[-2].rfind('.')
    return start, finish


def main() -> None:
    for name in ( 'data/23_input.txt', ):  # 'data/12_example.txt',
        field = tuple(read_file(name))

        new_line = ('#' * len(field[0]),)
        field = tuple(new_line) + field + tuple(new_line)
        start, finish = start_finish(field)
        # all_paths(field)  # I destroyed this function T_T
        # print(field)
        lines = find_lines(field, start, finish)
        count_longest_path(lines, start, finish)

        # 2306 is too low
        # 2354 is too low
        # 1749 not the right answer


if __name__ == '__main__':
    main()
