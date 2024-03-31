from common import get_data


def test_all() -> None:
    result = part_one('.^^.^.^^^^', 10)
    correct = 38
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(line: str, size: int = 2) -> int:
    # field = [line]
    total = line.count('.')
    size -= 1

    while size:
        size -= 1
        line = ''.join(('.', line, '.'))
        new_line = ''
        for i in range(len(line) - 2):
            first, second, third = line[i:i + 3]
            if (first != second and second == third) or \
                    (first == second and second != third):
                new_line += '^'
            else:
                new_line += '.'

        line = new_line
        total += line.count('.')

    return total


def main() -> None:
    data = get_data(2016, 18)[0]
    print('Part one:', part_one(data, 40))
    print('Part two:', part_one(data, 400000))


if __name__ == '__main__':
    test_all()
    main()
