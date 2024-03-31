from common import read_file, get_data

YEAR = 2017
DAY = 21


def test_all() -> None:
    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> dict:
    # A line of data looks like this:
    # ../.# => ##./#../...
    result = dict()
    for line in data:  # type: str
        pattern, replace = line.split(' => ')
        size = pattern.find('/')
        variations = ''.join(rotate_and_flip(pattern))
        pass


def repeat_pattern(pattern: tuple, size) -> tuple:
    return tuple(line * size for line in pattern) * size


def part_one(instructions: tuple, rotations: int = 1) -> None:
    pattern = tuple('.#./..#/###'.split('/'))
    print(*pattern, sep='\n')
    for _ in range(rotations):
        size = len(pattern) // 2 if not len(pattern) % 2 else len(pattern) // 3
        pattern = repeat_pattern(pattern, size)
        print(*pattern, sep='\n')


def rotate_and_flip(pattern: str) -> str:
    pattern = pattern.split('/')
    size = len(pattern)
    for _ in range(4):
        new_pattern = list()
        for i in range(size):
            new_pattern.append(''.join(pattern[ii][i] for ii in reversed(range(size))))
        yield ''.join(new_pattern)
        yield ''.join(reversed(new_pattern))
        pattern = new_pattern



def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    print('Part one:', part_one(data))
    # print('Part two:', )


if __name__ == '__main__':
    variations = '/'.join(frozenset(rotate_and_flip('.#./..#/###')))
    print(variations)
    start = '.#./..#/###'
    if start.replace('/', '') in variations:
        print('Success!')
    # test_all()
    # main()
