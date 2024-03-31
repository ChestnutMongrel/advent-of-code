from common import read_file, get_data, timer
from collections import defaultdict


YEAR = 2017
DAY = 18


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    instructions = parse_data(read_file('data/18_example.txt'))
    print(instructions)
    result = part_one(instructions)
    correct = 4
    assert correct == result, f'Should be {correct}, got {result} instead.'


def test_part_two() -> None:
    instructions = parse_data(read_file('data/18_example_2.txt'))
    print(instructions)
    result = part_two(instructions)
    correct = 3
    assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> tuple:
    instructions = list()
    with_register_and_value = ('set', 'add', 'mul', 'mod', 'jgz')
    with_one_value = ('snd', 'rcv')
    with_two_values = ('jgz',)

    for line in data:  # type: str
        command, first, *rest = line.split()  # type: str | int

        if command in with_register_and_value:
            second = rest[0]
            if not second.isalpha():
                second = int(second)

        elif command in with_one_value or command in with_two_values:
            if not first.isalpha():
                first = int(first)
            second = first

        if command in with_two_values:
            second = rest[0]
            if not second.isalpha():
                second = int(second)

        instructions.append((command, first, second))

    return instructions


@timer
def part_one(instructions: tuple) -> int | str:
    registers = defaultdict(int)
    number_of_instructions = len(instructions)
    index = 0
    sound = None

    while 0 <= index < number_of_instructions:
        command, first, second = instructions[index]
        match command:
            case 'snd':
                sound = registers[first] \
                    if type(first) == str \
                    else first

            case 'set':
                registers[first] = registers[second] \
                    if type(second) == str \
                    else second

            case 'add':
                registers[first] += registers[second] \
                    if type(second) == str \
                    else second

            case 'mul':
                registers[first] *= registers[second] \
                    if type(second) == str \
                    else second

            case 'mod':
                registers[first] %= registers[second] \
                    if type(second) == str \
                    else second

            case 'rcv':
                check_value = registers[first] if type(first) == str else first
                if check_value:
                    return sound

            case 'jgz':
                check_value = registers[first] if type(first) == str else first
                if check_value > 0:
                    index -= 1  # to contre +1 after
                    index += registers[second] if type(second) == str else second

            case _:
                print('unknown command', command)

        index += 1


def part_two(instructions: tuple) -> int:
    pass


def main() -> None:
    instructions = parse_data(get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(instructions))
    print('Part two:', part_two(instructions))


if __name__ == '__main__':
    test_all()
    main()
