from common import get_data

YEAR = 2017
DAY = 17


def test_all() -> None:
    data = 3

    check = (
        (part_one(data), 638),
        (part_two(data, 2017), 1226),
    )
    for result, correct in check:
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(steps: int, last_value: int = 2017) -> int:
    index = 0
    current = 0
    buffer = [current]

    while current < last_value:
        current += 1
        index = (index + steps) % current + 1
        buffer.insert(index, current)

    return buffer[index + 1]


# part_two took 8.569176110031549 secs
def part_two(steps: int, last_value: int) -> int:
    index = 0
    current = 0
    ind_after_zero = index + 1
    after_zero = 0

    while current < last_value:
        current += 1
        index = (index + steps) % current + 1
        if index == ind_after_zero:
            after_zero = current

    return after_zero


def main() -> None:
    data = int(get_data(year=YEAR, day=DAY)[0])
    print('Part one:', part_one(data))
    print('Part two:', part_two(data, 50_000_000))


if __name__ == '__main__':
    test_all()
    main()
