from common import read_file, get_data


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    data = tuple(read_file('data/02_example.txt'))
    result = part_one(data)
    correct = 18
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    data = tuple(read_file('data/02_example_part_two.txt'))
    result = part_two(data)
    correct = 9
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def count_max_difference(line: str) -> int:
    numbers = sorted(map(int, line.split()))
    return numbers[-1] - numbers[0]


def make_even_division(line: str) -> int:
    numbers = sorted(map(int, line.split()))
    for ind, first in enumerate(numbers):
        for second in numbers[ind + 1:]:
            if second % first == 0:
                return second // first
    return 0


def part_one(data: tuple[str]) -> int:
    return sum(map(count_max_difference, data))


def part_two(data: tuple[str]) -> int:
    return sum(map(make_even_division, data))


def main() -> None:
    data = get_data(2017, 2)
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
