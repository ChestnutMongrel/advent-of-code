from common import get_data, sum_tuple

YEAR = 2017
DAY = 22


def test_all() -> None:
    field = tuple('..#|#..|...'.split('|'))
    infected = parse_data(field)
    start = get_center(field)
    test_part_one(infected, start)
    test_part_two(infected, start)


def test_part_one(infected: tuple, start: tuple) -> None:
    check = (
        (7, 5),
        (70, 41),
        (10_000, 5587),
    )
    for repetitions, correct in check:
        result = part_one(set(infected), start, repetitions)
        assert correct == result, f'For {repetitions = } should be {correct}, got {result} instead.'


def test_part_two(infected: tuple, start: tuple) -> None:
    check = (
        (100, 26),
        (10000000, 2511944)
    )
    for repetitions, correct in check:
        result = part_two(set(infected), start, repetitions)
        assert correct == result, f'For {repetitions = } should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> tuple:
    mark = '#'
    marked = set()
    for i, line in enumerate(data):
        for ii, symbol in enumerate(line):
            if symbol == mark:
                marked.add((i, ii))
    return tuple(marked)


def get_center(data: tuple) -> tuple:
    return len(data) // 2, len(data[0]) // 2


def get_next_shift(index: int) -> tuple:
    shifts = ((-1, 0), (0, 1), (1, 0), (0, -1))
    number_shifts = len(shifts)
    index %= number_shifts
    return shifts[index]


# It took about 19 secs for 10_000_000 repetitions...
def part_one(infected: set, current: tuple, repetitions: int) -> int:
    number_infections: int = 0
    ind_turn = 0

    for _ in range(repetitions):
        if current in infected:
            ind_turn += 1
            infected.remove(current)
        else:
            ind_turn -= 1
            infected.add(current)
            number_infections += 1
        current = sum_tuple(current, get_next_shift(ind_turn))

    return number_infections


# It took 25.982910188962705 secs for 10_000_000 repetitions...
def part_two(infected: set, current: tuple, repetitions: int) -> int:
    number_infections: int = 0
    ind_turn = 0
    weakened = set()
    flagged = set()

    for _ in range(repetitions):
        if current in infected:
            ind_turn += 1
            infected.remove(current)
            flagged.add(current)

        elif current in flagged:
            ind_turn += 2
            flagged.remove(current)

        elif current in weakened:
            weakened.remove(current)
            infected.add(current)
            number_infections += 1

        else:  # if current is clean, i.e. everything else
            ind_turn -= 1
            weakened.add(current)

        current = sum_tuple(current, get_next_shift(ind_turn))

    return number_infections


def main() -> None:
    field = tuple(get_data(year=YEAR, day=DAY))
    infected = parse_data(field)
    start = get_center(field)
    print('Part one:', part_one(set(infected), start, 10_000))
    print('Part two:', part_two(set(infected), start, 10_000_000))


if __name__ == '__main__':
    test_all()
    main()
