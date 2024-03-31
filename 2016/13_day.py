from common import get_data, timer, sum_tuple
from functools import lru_cache


def test_is_open() -> None:
    check = (
        ((0, 0), True),
        ((1, 1), True),
        ((7, 4), True),
        ((8, 3), False),
        ((6, 2), False)
    )
    number = 10
    for data, correct in check:
        result = is_open(*data, number)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def test_part_one() -> None:
    number = 10
    part_one(number, (7, 4))


@lru_cache()
def is_open(x: int, y: int, number: int) -> bool:
    coeff = bin(x * x + 3 * x + 2 * x * y + y + y * y + number)
    return str(coeff).count('1') % 2 == 0


def print_maze(number: int) -> None:
    size = 40
    maze = [['.'] * size for _ in range(size)]

    for y in range(size):
        for x in range(size):
            if not is_open(x, y, number):
                maze[y][x] = '#'

    for line in maze:
        print(''.join(line))


def part_one(number: int, goal: tuple) -> tuple:
    start = (1, 1)
    size = max(goal) * 2
    maze = [[size ** 2] * size for _ in range(size)]
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

    if not is_open(*start, number):
        return -1, -1

    x, y = start
    maze[y][x] = 0

    to_move = [start]
    while to_move:
        new_to_move = list()
        for current in to_move:
            current_steps = maze[current[1]][current[0]]
            for move in moves:
                x, y = sum_tuple(current, move)
                if 0 <= x < size and 0 <= y < size and is_open(x, y, number):
                    if maze[y][x] > current_steps + 1:
                        new_to_move.append((x, y))
                        maze[y][x] = current_steps + 1
        to_move = new_to_move

    steps = 50
    can_be_reached = 0
    for x in range(size):
        for y in range(size):
            if maze[x][y] <= steps:
                can_be_reached += 1

    x, y = goal
    return maze[y][x], can_be_reached


def main() -> None:
    number = int(get_data(2016, 13)[0])
    goal = (31, 39)
    steps_to_goal, reached_in_50_steps = part_one(number, goal)
    print('Part one:', steps_to_goal)
    print('Part two:', reached_in_50_steps)


if __name__ == '__main__':
    test_is_open()
    test_part_one()
    main()
