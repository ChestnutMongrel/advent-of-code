from common import read_file, sum_tuple


def test_all() -> None:
    check = {
        '>': 2,
        '^>v<': 4,
        '^v^v^v^v^v': 2
    }

    for data, correct in check.items():
        result = count_houses(data)
        assert result == correct, f'Should be {correct}, got {result} instead.'

    check_two = {
        '^v': 3,
        '^>v<': 3,
        '^v^v^v^v^v': 11
    }

    for data, correct in check_two.items():
        result = count_houses(data, True)
        assert result == correct, f'Should be {correct}, got {result} instead.'


def count_houses_1(data: str) -> int:
    houses = dict()
    current = (0, 0)
    moves = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }

    houses[current] = 1
    for symbol in data:
        current = sum_tuple(current, moves[symbol])
        houses[current] = houses.get(current, 0) + 1

    return len(houses)


def count_houses(data: str, two: bool = False) -> int:
    houses = set()
    first = (0, 0)
    houses.add(first)

    moves = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }

    if not two:
        for symbol in data:
            first = sum_tuple(first, moves[symbol])
            houses.add(first)

    else:
        second = first
        for i in range(0, len(data) // 2 * 2, 2):
            first = sum_tuple(first, moves[data[i]])
            second = sum_tuple(second, moves[data[i + 1]])
            houses.add(first)
            houses.add(second)
        if len(data) % 2 == 1:
            houses.add(sum_tuple(first, moves[data[-1]]))

    return len(houses)


def main() -> None:
    name = 'data/03_input.txt'
    data = tuple(read_file(name))[0]
    print('Part one:', count_houses(data))
    print('Part two:', count_houses(data, True))


if __name__ == '__main__':
    test_all()
    main()
