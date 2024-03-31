from common import get_data, timer
from sympy import divisors


def test_count_presents() -> None:
    check = (
        (6, 12),
        (53, 53),
    )
    for data, correct in check:
        result = count_visitors(data, 50)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_all() -> None:
    check = (
        (10, 1),
        (60, 4),
        (120, 6),
        (80, 6)
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


# This obviously takes too long...
def part_one(num: int) -> int:
    num /= 10
    start = 1
    while True:
        if sum(divisors(start, True)) >= num:
            return start
        start += 1
        # print(start)


def count_visitors(num: int, limit: int) -> int:
    divs = divisors(num)
    total = sum(divs)
    for item in divs:
        if num / item > limit:
            total -= item
        else:
            return total
    return 0


@timer
def part_two(num: int) -> int:
    limit = 50
    per_num = 11

    upper = num // 11 + 1
    current = upper
    while current:
        if count_visitors(current, limit) * per_num >= num:
            upper = current
        current //= 2

    for i in range(upper // 2, upper):
        if count_visitors(i, limit) * per_num >= num:
            return i


def main() -> None:
    data = int(tuple(get_data(2015, 20))[0])
    # print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
    test_count_presents()

