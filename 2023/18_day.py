from common import read_file, sum_tuple


def find_start(plan: tuple) -> tuple:
    min_n = max_n = n = 0
    min_m = max_m = m = 0
    for direction, amount, _ in plan:
        match direction:
            case 'D':
                n += amount
                max_n = max(max_n, n)
            case 'U':
                n -= amount
                min_n = min(min_n, n)
            case 'R':
                m += amount
                max_m = max(max_m, m)
            case 'L':
                m -= amount
                min_m = min(min_m, m)

    start = -min_n + 1, -min_m + 1
    n = max_n - min_n + 3
    m = max_m - min_m + 3
    return start, n, m


def dig(plan: tuple) -> list:
    start, n, m = find_start(plan)

    # for item in field:
    #     print(''.join(item))

    field = [['.'] * m for _ in range(n)]
    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0)
    }

    x, y = start
    field[x][y] = '#'

    # for item in field:
    #     print(''.join(item))

    for item in plan:
        for _ in range(item[1]):
            x, y = sum_tuple((x, y), moves[item[0]])
            field[x][y] = '#'

    return field


def create_field(plan: tuple) -> list:

    start, n, m = find_start(plan)
    field = [['.'] * m for _ in range(n)]

    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0)
    }

    x, y = start
    last = plan[-1][0]
    for item in plan:
        current = item[0]
        corner, symbol = what_symbol(last, current)
        field[x][y] = corner
        for _ in range(item[1]):
            x, y = sum_tuple((x, y), moves[item[0]])
            field[x][y] = symbol
        last = current
    field[x][y] = what_symbol(last, plan[0][0])[0]
    return field


def what_symbol(first: str, second: str) -> tuple:
    if (first, second) in (('L', 'D'), ('U', 'R')):
        corner = '╔'
    elif (first, second) in (('R', 'D'), ('U', 'L')):
        corner = '╗'
    elif (first, second) in (('D', 'L'), ('R', 'U')):
        corner = '╝'
    elif (first, second) in (('D', 'R'), ('L', 'U')):
        corner = '╚'
    if second in ('R', 'L'):
        symbol = '═'
    else:
        symbol = '║'
    return corner, symbol


def read_plan(data: str) -> tuple:
    direction, amount, colour = data.split()
    amount = int(amount)
    return direction, amount, colour


def fill_field(field: list) -> list:
    # for i, line in enumerate(field):
    #     inside = False
    #     last = '.'
    #     for ii, symbol in enumerate(line):
    #         if symbol == '#':
    #             # if last == '#':
    #             #     continue
    #             inside = True
    #         else:
    #             if last == '#' and field[i-1][ii] == '.':
    #                 inside = False
    #             if inside:
    #                 field[i][ii] = '#'
    #         last = symbol
    # return field
    pass


def count_capacity(field: list) -> int:
    # capacity = 0
    # for line in field:
    #     inside = False
    #     last = '.'
    #     for symbol in line:
    #         if inside or symbol == '#':
    #             capacity += 1
    #         if symbol == '#' and last == '.':
    #             inside = not inside
    #         last = symbol
    #     print(capacity)
    # return capacity
    capacity = 0
    for line in field:
        capacity += ''.join(line).count('#')
    return capacity


def count_inside(field: list) -> int:
    total = 0
    switch = ({'╚', '╗'}, {'╔', '╝'})

    for x in range(1, len(field) - 1):
        outside = True
        prev_node = ''
        for y in range(1, len(field[0]) - 1):
            if field[x][y] != '.':
                total += 1
                symbol = field[x][y]
                if symbol == '║':
                    outside = not outside
                elif symbol == '═':
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


def convert_plan(plan: tuple) -> tuple:
    colour = plan[-1].replace('(#', '').replace(')', '')
    number = int(colour[:-1], 16)
    directions = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    return directions[colour[-1]], number, ''


def main() -> None:
    for name in ('data/12_example.txt', 'data/18_input.txt'):
        plan = tuple(read_plan(data) for data in read_file(name))
        # print(*plan, sep='\n')
        field = create_field(plan)
        # for item in field:
        #     print(''.join(item))

        print(count_inside(field))

        new_plan = tuple(convert_plan(item) for item in plan)
        print(new_plan)
        print(find_start(new_plan))


if __name__ == '__main__':
    main()
