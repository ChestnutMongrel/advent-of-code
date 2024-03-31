from common import get_data, sum_tuple


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    check = (
        ('R2, L3', 5),
        ('R2, R2, R2', 2),
        ('R5, L5, R5, R3', 12)
    )
    for data, correct in check:
        result = part_one(tuple(data.split(', ')))
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    data = 'R8, R4, R4, R8'
    correct = 4
    result = part_two(data.split(', '))
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


# Variables naming is awful >_<
def part_one(data: tuple) -> int:
    turn = ((0, -1), (1, 0), (0, 1), (-1, 0))
    current_turn = 0

    current = (0, 0)
    for line in data:
        to_turn = line[0]
        amount = int(line[1:])
        if to_turn == 'R':
            current_turn += 1
        else:
            current_turn -= 1
        current_turn = current_turn % 4
        to_go = turn[current_turn][0] * amount, turn[current_turn][1] * amount
        current = sum_tuple(current, to_go)

    return abs(current[0]) + abs(current[1])


def part_two(data: tuple) -> int:
    turn = ((0, -1), (1, 0), (0, 1), (-1, 0))
    current_turn = 0
    visited = set()

    current = (0, 0)
    visited.add(current)

    for line in data:
        to_turn = line[0]
        amount = int(line[1:])
        if to_turn == 'R':
            current_turn += 1
        else:
            current_turn -= 1
        for i in range(amount):
            current = sum_tuple(current, turn[current_turn % 4])
            if current in visited:
                return abs(current[0]) + abs(current[1])
            else:
                visited.add(current)


def main() -> None:
    data = tuple(get_data(2016, 1)[0].split(', '))
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
