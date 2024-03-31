from common import read_file, get_data, timer


def test_all() -> None:
    data = tuple(read_file('data/23_example.txt'))
    correct = 3
    result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'


@timer
def part_one(data: tuple, **kwargs) -> int:
    # a = b = c = d = 0
    registers = dict().fromkeys('abcd', 0)
    for key, value in kwargs.items():
        registers[key] = value
    length = len(data)
    ind = 0
    data = list(data)

    while 0 <= ind < length:
        instruction, first, *second = data[ind].split()
        match instruction:
            case 'cpy':
                second = second[0]
                if second in registers:
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
                    second = second[0]
                    if second in registers:
                        # Should I ignore this part? Apparently not...
                        ind += registers[second] - 1
                    else:
                        ind += int(second) - 1

            case 'tgl':
                if first in registers:
                    ind_to_change = ind + registers[first]
                else:
                    ind_to_change = ind + int(first)
                if ind_to_change < length:
                    instr = data[ind_to_change].split()
                    if len(instr) == 2:
                        replacing = 'dec' if instr[0] == 'inc' else 'inc'
                    else:  # if len(instr) == 3:
                        replacing = 'cpy' if instr[0] == 'jnz' else 'jnz'
                    new_instr = ' '.join((replacing, *instr[1:]))
                    data[ind_to_change] = new_instr

        ind += 1

    return registers['a']


def main() -> None:
    data = get_data(2016, 23)
    print('Part one:', part_one(data, a=7))
    # part_one took 246.962331804999849 secs
    # a = 11: 39923508
    print('Part two:', part_one(data, a=12))


if __name__ == '__main__':
    test_all()
    main()
