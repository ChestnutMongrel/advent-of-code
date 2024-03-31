from common import read_file, get_data, timer
from string import ascii_lowercase


YEAR = 2017
DAY = 16


def test_all() -> None:
    moves = tuple(read_file('data/16_example.txt'))
    check = (
        ((moves, 5), 'baedc'),
        ((moves, 5, 2), 'ceadb')
    )
    for data, correct in check:
        result = part_one(*data)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def rewrite_instructions(data: tuple) -> tuple:
    spin_exchange = list()
    partner = list()

    for line in data:  # type: str
        if line.startswith('s'):
            shift = int(line[1:])
            spin_exchange.append(('spin', shift, shift))

        elif line.startswith('x'):
            first, second = map(int, line[1:].split('/'))
            spin_exchange.append(('exchange', first, second))

        elif line.startswith('p'):
            partner.append(tuple(line[1:].split('/')))

    return tuple(spin_exchange), tuple(partner)


@timer
def part_one(moves: tuple, size: int, repeat: int = 1) -> str:
    line = list(ascii_lowercase[:size])

    for _ in range(repeat):
        print(''.join(line))
        for symbol, *values in moves:  # type: str
            values = ''.join(values)
            if symbol == 's':
                shift = int(values)
                line = line[-shift:] + line[:-shift]
            else:
                if symbol == 'x':
                    ind_a, ind_b = map(int, values.split('/'))
                elif symbol == 'p':
                    name_a, name_b = values.split('/')
                    ind_a = line.index(name_a)
                    ind_b = line.index(name_b)
                line[ind_a], line[ind_b] = line[ind_b], line[ind_a]

    return ''.join(line)


def main() -> None:
    data = get_data(year=YEAR, day=DAY)[0].split(',')
    spin_exchange, partner = rewrite_instructions(data)
    print(f'{len(spin_exchange) = }')
    print(f'{len(partner) = }')
    # print('Part one:', part_one(data, 16))
    print('Part two:', part_one(data, 16, 10))


if __name__ == '__main__':
    # test_all()
    main()
