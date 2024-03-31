from common import read_file, sum_tuple, find_start
import functools
import time


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper


def step(garden: tuple, current: set, only_in: bool = False) -> set:
    moves = ((0, 1), (0, -1), (-1, 0), (1, 0))
    new_places = set()
    rows = len(garden)
    columns = len(garden[0])

    for place in current:
        for move in moves:
            x, y = sum_tuple(place, move)
            symbol = garden[x % rows][y % columns]
            if symbol in '.S':
                new_places.add((x, y))

    return new_places


@timer
def go_wild(garden: tuple, steps: int) -> int:
    current = two_steps_before = {find_start(garden)}
    one_step_before = set()

    for i in range(steps // 2):
        current = step(garden, current)
        current -= one_step_before
        one_step_before.update(current)

        current = step(garden, current)
        current -= two_steps_before
        two_steps_before.update(current)

    if steps % 2 == 1:
        current = step(garden, current)
        current -= one_step_before
        one_step_before.update(current)
        current.update(one_step_before)
    else:
        current.update(two_steps_before)
    return len(current)


def test_go_wild(garden: tuple) -> None:
    checks = {6: 16, 10: 50, 50: 1594, 100: 6536,
              500: 167004}  #, 1000: 668697}  #, 5000: 16_733_044}
    for key, value in checks.items():
        print(key)
        assert go_wild(garden, key) == value


@timer
def find_cycles(garden: tuple) -> tuple:
    current = {find_start(garden)}
    start = find_start(garden)
    first_cycle = list()
    second_cycle = list()
    i = 0
    while True:
        i += 1
        current = step(garden, current, True)
        if current in first_cycle:
            if current in second_cycle:
                print(first_cycle == second_cycle)
                break
            else:
                second_cycle.append(current)
        else:
            first_cycle.append(current)
        if i == 100:
            print(first_cycle)
            break


def main() -> None:
    for name in ('data/12_example.txt',):  # 'data/21_input.txt'):
        garden = tuple(read_file(name))
        # print(*garden, sep='\n')
        # start = find_start(garden)
        goal = 26501365

        # print(go_wild(garden, 6))
        # current = {start}
        # for _ in range(steps):
        #     current = step(garden, current)
        # print(len(current))
        # test_go_wild(garden)

        # print(find_cycles(garden))
        for i in range(1, 6):
            print(i * 17, go_wild(garden, i * 17))

        # print('42', go_wild(garden, 42))
        # print('63', go_wild(garden, 63))


if __name__ == '__main__':
    main()
