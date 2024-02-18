from common import get_data, sum_tuple
from hashlib import md5


def test_all() -> None:
    test_part_one()
    test_part_two()


def test_part_one() -> None:
    check = (
        ('hijkl', ''),
        ('ihgpwlah', 'DDRRRD'),
        ('kglvqrro', 'DDUDRLRRUDRD'),
        ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    check = (
        ('ihgpwlah', 370),
        ('kglvqrro', 492),
        ('ulqzkmiv', 830)
    )
    for data, correct in check:
        result = part_one(data, longest=True)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(passcode: str, longest: bool = False) -> str | int:
    goal = (3, 3)
    size = 4
    start = (0, 0)
    moves = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    opened = 'bcdef'
    paths = {'': start}
    longest_path = 0

    while paths:
        new_paths = dict()
        for path, start in paths.items():
            doors = md5(''.join((passcode, path)).encode()).hexdigest()[:size]
            for i, direction in enumerate(moves):
                if doors[i] in opened:
                    new_path = ''.join((path, direction))
                    current = x, y = sum_tuple(start, moves[direction])
                    if 0 <= x < size and 0 <= y < size:
                        if current == goal:
                            if not longest:
                                return new_path
                            elif len(new_path) > longest_path:
                                longest_path = len(new_path)
                        else:
                            new_paths[new_path] = current

        paths = new_paths

    if longest:
        return longest_path
    else:
        return ''


def main() -> None:
    data = get_data(2016, 17)[0]
    print('Part one:', part_one(data))
    print('Part two:', part_one(data, longest=True))


if __name__ == '__main__':
    test_all()
    main()
