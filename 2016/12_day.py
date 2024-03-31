from common import read_file, get_data


def test_all() -> None:
    data = tuple(read_file('data/12_example.txt'))
    correct = 42
    result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'


# It would be nice to find circle and shorten it
def part_one(data: tuple, c: int = 0) -> int:
    # a = b = c = d = 0
    registers = dict().fromkeys('abcd', 0)
    registers['c'] = c
    length = len(data)
    ind = 0

    while 0 <= ind < length:
        instruction, first, *second = data[ind].split()
        match instruction:
            case 'cpy':
                second = second[0]
                if first in registers:
                    registers[second] = registers[first]
                else:
                    registers[second] = int(first)

            case 'inc':
                registers[first] += 1
            case 'dec':
                registers[first] -= 1

            case 'jnz':
                if (first in registers and registers[first]) or \
                        (first not in registers and first != '0'):
                    # -1 is for counteract the ind += 1 later.
                    ind += int(second[0]) - 1

        ind += 1

    return registers['a']


def main() -> None:
    data = get_data(2016, 12)
    print('Part one:', part_one(data))
    print('Part two:', part_one(data, c=1))


if __name__ == '__main__':
    test_all()
    main()
