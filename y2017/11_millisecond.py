"""
Long live the author:
https://www.redblobgames.com/grids/hexagons/
"""


from common import read_file, get_data, sum_tuple

YEAR = 2017
DAY = 11


def test_all() -> None:
    check = (
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3)
    )
    for data, correct in check:
        result = part_one(tuple(data.split(',')))
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


# This function looked way better before the part two (the furthest distance counting)...
def move_through(path: tuple) -> tuple:
    moves = {
        'n':  (1, 0, -1),
        'nw': (1, -1, 0),
        'ne': (0, 1, -1),
        's':  (-1, 0, 1),
        'sw': (0, -1, 1),
        'se': (-1, 1, 0)
    }

    current = (0, 0, 0)
    furthest = find_distance(current)
    for step in path:
        current = sum_tuple(current, moves[step])
        distance = find_distance(current)
        if distance > furthest:
            furthest = distance

    print(f'{furthest = }')

    return current


def find_distance(first: tuple, second: tuple = None) -> int:
    if second:
        pass

    return max(map(abs, first))


def part_one(data: tuple) -> int:
    coordinate = move_through(data)
    return find_distance(coordinate)


def main() -> None:
    data = tuple(get_data(year=YEAR, day=DAY)[0].split(','))
    print('Part one:', part_one(data))
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
