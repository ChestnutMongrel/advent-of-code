from common import read_file, get_data


def test_all() -> None:
    data = list(read_file('data/07_example.txt'))
    correct = 0
    result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: list) -> int:
    wires = dict()
    operators = ('AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT')
    new_data = data.copy()

    while new_data:
        not_used = list()

        for line in new_data:
            instructions, wire = line.split(' -> ')
            values = instructions.split()

            for i, item in enumerate(values):
                if item not in operators:
                    if item.isdigit():
                        values[i] = int(item)
                    elif item not in wires:
                        not_used.append(line)
                        break
                    else:
                        values[i] = wires[item]
            else:
                if len(values) == 1:
                    result = values[0]
                elif len(values) == 2:
                    result = ~values[-1]
                else:
                    first, operator, second = values
                    match operator:
                        case 'AND':
                            result = first & second
                        case 'OR':
                            result = first | second
                        case 'LSHIFT':
                            result = first << second
                        case 'RSHIFT':
                            result = first >> second
                # if result < 0:
                #     result += 65536
                wires[wire] = result

        new_data = not_used.copy()

    return wires.get('a', 0)


def main() -> None:
    data = list(get_data(2015, 7))
    result = part_one(data)
    print('Part one:', result)

    for item in data:
        if item.endswith('-> b'):
            data.remove(item)
            break
    data.insert(0, f'{result} -> b')
    result_two = part_one(data)
    print('Part two:', result_two)


if __name__ == '__main__':
    test_all()
    main()
