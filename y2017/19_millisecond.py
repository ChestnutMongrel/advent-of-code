from common import read_file, get_data, sum_tuple

YEAR = 2017
DAY = 19


def test_all() -> None:
    data = tuple(read_file('data/19_example.txt'))
    for line in data:
        print('!', line, '!')

    result = part_one(data)
    correct = ('ABCDEF', 38)
    assert correct == result, f'Should be {correct}, got {result} instead.'

    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(data: tuple[str]) -> tuple:
    path = '|-+'
    collected = list()
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    ind_move = 0
    num_move = len(moves)

    depth = len(data)

    current = (0, data[0].find('|'))
    steps = 1

    while True:
        current = x, y = sum_tuple(current, moves[ind_move])

        if data[x][y] == ' ':
            return ''.join(collected), steps

        if data[x][y] not in path:
            collected.append(data[x][y])

        elif data[x][y] == '+':
            right = (ind_move - 1) % num_move
            x, y = sum_tuple(current, moves[right])
            if x < depth and y < len(data[x]) and data[x][y] != ' ':
                ind_move = right
            else:
                ind_move = (ind_move + 1) % num_move

        steps += 1


def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    symbols, steps = part_one(data)
    print('Part one:', symbols)
    print('Part two:', steps)


if __name__ == '__main__':
    test_all()
    main()
