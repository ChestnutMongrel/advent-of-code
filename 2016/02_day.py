from common import get_data, sum_tuple


KEYPAD_3x3 = (
    '123',
    '456',
    '789'
)

KEYPAD_DIAMOND = (
    '__1__',
    '_234_',
    '56789',
    '_ABC_',
    '__D__'
)


def test_all() -> None:
    instructions = '''ULL
RRDDD
LURDL
UUUUD'''
    data = tuple(instructions.split('\n'))

    result = part_one(data)
    correct = '1985'
    assert correct == result, f'Should be {correct}, got {result} instead.'

    result = part_one(data, keypad=KEYPAD_DIAMOND)
    correct = '5DB3'
    assert correct == result, f'Should be {correct}, got {result} instead.'


def find_symbol(data: tuple, symbol: str) -> tuple:
    for ind, line in enumerate(data):  # type: str
        if symbol in line:
            return ind, line.index(symbol)


def part_one(data: tuple, keypad: tuple = KEYPAD_3x3) -> str:
    moves = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }

    size = len(keypad)

    current = find_symbol(keypad, '5')

    code = ''
    for line in data:
        for symbol in line:
            x, y = sum_tuple(current, moves[symbol])
            if 0 <= x < size and 0 <= y < size:
                if keypad[x][y] != '_':
                    current = x, y
        x, y = current
        code += keypad[x][y]

    return code


def main() -> None:
    data = get_data(2016, 2)
    print('Part one:', part_one(data))
    print('Part two:', part_one(data, keypad=KEYPAD_DIAMOND))


if __name__ == '__main__':
    test_all()
    main()
