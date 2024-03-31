from common import read_file, get_data


def test_all() -> None:
    data = tuple(map(read_instructions, read_file('data/23_example.txt')))
    result = part_one(data)
    correct = 0
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(instructions: tuple, a: int = 0) -> int:
    registers = {'a': a, 'b': 0}
    index = 0
    amount = len(instructions)

    while index < amount:
        instr, name, num = instructions[index]
        match instr:
            case 'hlf':
                registers[name] //= 2

            case 'tpl':
                registers[name] *= 3

            case 'inc':
                registers[name] += 1

            # In all jumps there is a '-1' for index statement to contre 'index += 1 later.
            case 'jmp':
                index += num - 1

            # In jumps with condition if it is not true one should just get the next index.
            case 'jie':
                if registers[name] % 2 == 0:
                    index += num - 1

            case 'jio':
                if registers[name] == 1:
                    index += num - 1

            case _:
                break

        index += 1

    return registers['b']


def read_instructions(line: str) -> tuple:
    instr, register, *num = line.replace(',', '').split()

    if num:
        num = int(num[0])

    elif register[0] in ('+', '-'):
        num = int(register)
        register = ''

    else:
        num = 0

    return instr, register, num


def main() -> None:
    data = tuple(map(read_instructions, get_data(2015, 23)))
    print('Part one:', part_one(data))
    print('Part two:', part_one(data, 1))


if __name__ == '__main__':
    test_all()
    main()
