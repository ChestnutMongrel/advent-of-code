from common import get_data, timer
from re import search


def test_all() -> None:
    first_few = (20151125, 31916031, 18749137, 16080970, 21629792, 17289845, 24592653, 8057251, 16929656, 30943339)
    codes = get_code()
    for correct in first_few:
        result = next(codes)
        assert correct == result, f'Should be {correct}, got {result} instead.'

    check = (
        ((3, 1), 6),
        ((1, 3), 4),
        ((2, 5), 17),
        ((5, 4), 33)
    )
    for data, correct in check:
        result = serial_number(*data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'

    check = (
        ((3, 3), 1601130),
        ((5, 3), 11661866),
        ((6, 6), 27995004)
    )
    for data, correct in check:
        number = serial_number(*data)
        gen = get_code()
        for _ in range(number - 1):
            next(gen)
        result = next(gen)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def get_code() -> int:
    first = 20151125
    multiplier = 252533
    divisor = 33554393

    while True:
        yield first
        first = first * multiplier % divisor


def serial_number(column: int, row: int) -> int:
    number = sum(range(column + 1)) + sum(range(row - 1)) + column * (row - 1)
    return number


def get_column_row(line: str) -> tuple:
    column = int(search(r'(?<=column )\d+', line).group())
    row = int(search(r'(?<=row )\d+', line).group())
    return column, row


@timer
def main() -> None:
    data = get_data(2015, 25)[0]
    column, row = get_column_row(data)

    gen = get_code()
    for i in range(serial_number(column, row) - 1):
        next(gen)
    print('Part one:', next(gen))


if __name__ == '__main__':
    test_all()
    main()
