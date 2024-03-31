from common import read_file, get_data
from collections import defaultdict

YEAR = 2017
DAY = 23


def test_all() -> None:
    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple[str]) -> tuple:
    # A line of the data looks like this:
    # sub b -100000
    instructions = list()
    for line in data:
        command, first, second = line.split()
        if not first.isalpha():
            first = int(first)
        if not second.isalpha():
            second = int(second)
        instructions.append((command, first, second))
    return tuple(instructions)


def part_one(instructions: tuple) -> None:
    registers = defaultdict(int)
    mul_invoked = 0
    index = 0
    number_instructions = len(instructions)

    while 0 <= index < number_instructions:
        command, first, second = instructions[index]
        value = second if type(second) == int else registers[second]
        match command:
            case 'set':
                registers[first] = value
            case 'sub':
                registers[first] -= value
            case 'mul':
                registers[first] *= value
                mul_invoked += 1
            case 'jnz':
                first_value = first if type(first) == int else registers[first]
                if first_value:
                    index += value - 1
        index += 1

    return mul_invoked


def main() -> None:
    data = parse_data(get_data(year=YEAR, day=DAY))
    print(*data, sep='\n')
    print('Part one:', part_one(data))
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
