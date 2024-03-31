from functools import lru_cache


def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip()


# Why is there a mistake with tuple indexes here with the decorator?
# @lru_cache()
def turn(pattern: tuple) -> tuple:
    for i in range(len(pattern[0])):
        yield ''.join(line[i] for line in pattern)


@lru_cache()
def move_rocks(field: tuple, left: bool = True) -> tuple:
    new_field = list()
    len_line = len(field[0])
    for line in field:
        rocks = 0
        empty = 0
        new_line = ''
        for i in range(len(line)):
            symbol = line[i] if left else line[len_line - 1 - i]
            if symbol == '#':
                if left:
                    new_line += 'O' * rocks + '.' * empty + '#'
                else:
                    new_line = '#' + '.' * empty + 'O' * rocks + new_line
                rocks = empty = 0
            elif symbol == 'O':
                rocks += 1
            else:  # if symbol == '.':
                empty += 1
        if left:
            new_line += 'O' * rocks + '.' * empty
        else:
            new_line = '.' * empty + 'O' * rocks + new_line
        new_field.append(new_line)
    return tuple(new_field)


def count_load(field: tuple) -> int:
    load = 0
    weight = len(field)
    for line in field:
        load += weight * line.count('O')
        weight -= 1
    return load


@lru_cache()
def full_cycle(field: tuple) -> tuple:

    # Move rocks to the north (the field is turned)
    field = tuple(turn(field))
    field = move_rocks(field)
    # Move rocks to the west
    field = tuple(turn(field))
    field = move_rocks(field)
    # Move rocks to the south (the field is turned)
    field = tuple(turn(field))
    field = move_rocks(field, False)
    # Move rocks to the east
    field = tuple(turn(field))
    field = move_rocks(field, False)
    return field


def main() -> None:
    # Should be 1_000_000_000, but it's actually enough to do 1_000.
    cycles = 1_000_000_000

    for name in ('data/14_input.txt',):
        field = tuple(read_file(name))

        for i in range(10_000):
            print(i)
            for _ in range(cycles // 10_000):
                field = full_cycle(field)

        print('total load:', count_load(field))


if __name__ == '__main__':
    main()
