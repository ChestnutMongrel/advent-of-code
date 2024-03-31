from common import read_file, get_data, timer

YEAR = 2017
DAY = 15


def test_all() -> None:
    values = (65, 8921)
    check = (
        # (part_one(*values), 588),
        (part_two(*values), 309),
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(line: str) -> int:
    *_, digits = line.split()
    return int(digits)


@timer
def part_one(number_a: int, number_b: int) -> int:
    factor_a = 16_807
    factor_b = 48_271
    divisor = 2_147_483_647
    pairs = 40_000_000
    compare_size = 16
    match = 0

    for _ in range(pairs):
        number_a = (number_a * factor_a) % divisor
        number_b = (number_b * factor_b) % divisor
        if bin(number_a)[-compare_size:] == bin(number_b)[-compare_size:]:
            match += 1

    return match


@timer
def part_two(number_a: int, number_b: int) -> int:
    factor_a = 16_807
    factor_b = 48_271
    divisor_a = 4
    divisor_b = 8
    divisor = 2_147_483_647
    pairs = 5_000_000
    compare_size = 16
    match = 0

    for _ in range(pairs):
        while (number_a := (number_a * factor_a) % divisor) % divisor_a:
            continue
        while (number_b := (number_b * factor_b) % divisor) % divisor_b:
            continue
        if bin(number_a)[-compare_size:] == bin(number_b)[-compare_size:]:
            match += 1

    return match


def main() -> None:
    start_a, start_b = map(parse_data, get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(start_a, start_b))
    print('Part two:', part_two(start_a, start_b))


if __name__ == '__main__':
    test_all()
    main()
