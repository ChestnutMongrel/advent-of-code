from common import read_file, get_data
from collections import defaultdict


YEAR = 2017
DAY = 8


def test_all() -> None:
    data = tuple(read_file('data/08_example.txt'))
    result = part_one(data)
    correct = 1, 10
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: tuple) -> tuple:
    # The line of data looks like this:
    # anb inc 852 if mk == 789

    registers = defaultdict(int)
    highest_value = 0

    operations = {
        '==': int.__eq__,
        '!=': int.__ne__,
        '<':  int.__lt__,
        '>':  int.__gt__,
        '<=': int.__le__,
        '>=': int.__ge__,
    }

    for line in data:  # type: str
        current, _, value, _, cond_register, cond_sign, cond_value = line.split()
        value = int(value)
        cond_value = int(cond_value)

        if 'dec' in line:
            value *= -1

        if operations[cond_sign](registers[cond_register], cond_value):
            registers[current] += value
            if registers[current] > highest_value:
                highest_value = registers[current]

    return max(registers.values()), highest_value


def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    current_highest, ever_highest = part_one(data)
    print('Part one:', current_highest)
    print('Part two:', ever_highest)


if __name__ == '__main__':
    test_all()
    main()
