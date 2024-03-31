from common import read_file, get_data


def test_all() -> None:
    test_rotate()

    data = 'abcde'
    instructions = tuple(read_file('data/21_example.txt'))
    result = part_one(data, instructions)
    correct = 'decab'
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'

    print()
    result = part_one(correct, reversed(instructions), reversing=True)
    assert result == data, f'For {correct} should be {data}, got {result} instead.'


def test_rotate() -> None:
    data = '01234567'
    instruction = 'rotate based on position of letter '

    check = (
        ('0', '70123456'),
        ('7', '70123456'),
        ('4', '23456701'),
        ('3', '45670123'),
        ('6', data)
    )

    for symbol, correct in check:
        result = part_one(data, (instruction + symbol,))
        assert correct == result, f'For {symbol} should be {correct}, got {result} instead.'

    for symbol, password in check:
        result = part_one(password, (instruction + symbol,), reversing=True)
        assert data == result, f'For {symbol} should be {data}, got {result} instead.'


def part_one(password: str, instructions: tuple, reversing: bool = False) -> str:
    result = password
    print(f'{result = }')

    for line in instructions:  # type: str
        print(f'{line = }')
        if line.startswith('swap'):
            line = line.split()
            first = line[2]
            second = line[-1]
            if 'position' in line:
                first, second = map(int, (first, second))
                result = list(result)
                result[first], result[second] = result[second], result[first]
                result = ''.join(result)
            elif 'letter' in line:
                result = result.replace(first, ' ').replace(second, first).replace(' ', second)

        elif line.startswith('rotate'):
            if 'step' in line:
                steps = int(line.split()[-2])
                if 'right' in line:
                    steps *= -1
                if reversing:
                    steps *= -1
            elif 'letter' in line:
                letter = line.split()[-1]
                index = result.find(letter)
                if reversing:
                    for old_index in range(len(password)):
                        shift = 1 + old_index + int(old_index >= 4)
                        if (shift + old_index) % len(password) == index:
                            steps = shift
                            print('shift', shift)
                            break
                else:
                    steps = -(1 + index + int(index >= 4))
                # print('steps in letter', steps)
                steps %= len(password)
            result = result[steps:] + result[:steps]

        elif line.startswith('reverse'):
            line = line.split()
            first = int(line[2])
            second = int(line[-1]) + 1
            result = result[:first] + ''.join(reversed(result[first:second])) + result[second:]

        elif line.startswith('move'):
            result = list(result)
            line = line.split()
            first = int(line[2])
            second = int(line[-1])
            if reversing:
                first, second = second, first
            letter = result.pop(first)
            result.insert(second, letter)
            result = ''.join(result)

        print(f'{result = }')

    return result


def main() -> None:
    print('!!!')
    instructions = get_data(2016, 21)
    password = 'abcdefgh'
    print('Part one:', part_one(password, instructions))
    backward = 'fbgdceah'
    print('Part two:', part_one(backward, reversed(instructions), True))


if __name__ == '__main__':
    # test_all()
    main()
