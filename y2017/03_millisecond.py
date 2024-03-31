from common import get_data, sum_tuple, timer


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    check = (
        (12, 3),
        (1, 0),
        (25, 4),
        (23, 2),
        (1024, 31)
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    check = (
        (1, 1),
        (6, 10),
        (69, 122),
        (13, 23)
    )
    for data, correct in check:
        result = part_two(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(number: int) -> int:
    square_size = int(number ** 0.5)
    if square_size % 2 == 0:
        square_size -= 1
    current_coordinate = (square_size // 2,) * 2

    if number != square_size ** 2:
        path = tuple(go_around(current_coordinate, square_size))
        current_coordinate = path[number - square_size ** 2 - 1]

    x, y = map(abs, current_coordinate)
    return x + y


def part_two(number: int) -> int:
    current = (0, 0)
    value = size = 1
    matrix = {current: value}

    while True:
        for coordinate in go_around(current, size):
            value = 0
            for neighbor in go_around(coordinate):
                value += matrix.get(neighbor, 0)
            if value >= number:
                return value
            matrix[coordinate] = value
        else:
            current = coordinate
        size += 2


def go_around(current: tuple, size: int = 1) -> tuple:
    directions = {
        'up': (-1, 0),
        'left': (0, -1),
        'down': (1, 0),
        'right': (0, 1)
    }
    current = sum_tuple(current, (1, 1))
    for coordinates in directions.values():
        for _ in range(size + 1):
            current = sum_tuple(current, coordinates)
            yield current


def main() -> None:
    data = int(get_data(2017, 3)[0])
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
