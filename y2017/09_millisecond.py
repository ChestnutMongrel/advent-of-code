from common import read_file, get_data
import re


YEAR = 2017
DAY = 9


def test_all() -> None:
    test_find_garbage()
    test_part_one()
    test_count_symbols()


def test_part_one() -> None:
    check = (
        ('{}', 1),
        ('{{{}}}', 6),
        ('{{},{}}', 5),
        ('{{{},{},{{}}}}', 16),
        ('{<a>,<a>,<a>,<a>}', 1),
        ('{{<!>},{<!>},{<!>},{<a>}}', 3),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
        ('{{<}!>},{<}!>},{<}!>},{<a}>}}', 3),
    )
    for line, correct in check:
        clean_line, _ = remove_and_count(line)
        result = part_one(clean_line)
        assert correct == result, f'For {line} should be {correct}, got {result} instead.'


def test_find_garbage() -> None:
    data = tuple(read_file('data/garbage.txt'))
    for line in data:
        result = find_garbage(line)
        assert line == result, f'Should be {line}, got {result} instead.'

    check = (
        ('{<{},{},{{}}>}', '<{},{},{{}}>'),
        ('{{<!>},{<!>},{<!>},{<a>}}', '<!>},{<!>},{<!>},{<a>'),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', '<!!>'),
        ('{{!<!!>},{!<!!>},{!<!!>},{!<!!>}}', '')
    )
    for line, correct in check:
        result = find_garbage(line)
        assert correct == result, f'For {line} should be {correct}, got {result} instead.'


def test_count_symbols() -> None:
    data = read_file('data/garbage.txt')
    correct_answers = (0, 17, 3, 2, 0, 0, 10)
    for line, correct in zip(data, correct_answers):
        _, result = remove_and_count(line)
        assert correct == result, f'For {line} should be {correct}, got {result} instead.'


def is_canceled(line: str, ind: int) -> bool:
    if ind == 0:
        return False

    if ind == 1:
        return line[0] == '!'

    pattern = re.compile(f'!+$')
    if match := pattern.search(line[:ind]):
        return bool(len(match.group()) % 2)
    return False


def find_garbage(line: str) -> str:
    start = finish = -1

    while True:
        start = line.find('<', start + 1)
        if start == -1 or not is_canceled(line, start):
            break
    while start != -1:
        finish = line.find('>', finish + 1)
        if not is_canceled(line, finish):
            break

    return line[start:finish + 1]


def remove_and_count(line: str) -> tuple[str, int]:
    total = 0
    while garbage := find_garbage(line):
        line = line.replace(garbage, '', 1)
        garbage = garbage[1:-1]
        while (ind := garbage.find('!')) != -1:
            canceled = garbage[ind:ind + 2]
            garbage = garbage.replace(canceled, '', 1)
        total += len(garbage)
    return line, total


def part_one(line: str) -> int:
    total_score = 0
    group = 0
    opening = '{'
    closing = '}'
    for ind, symbol in enumerate(line):
        if symbol == opening:
            group += 1
        elif symbol == closing:
            total_score += group
            group -= 1
    return total_score


def main() -> None:
    data = get_data(year=YEAR, day=DAY)[0]
    clean_data, amount_removed_symbols = remove_and_count(data)
    print('Part one:', part_one(clean_data))
    print('Part two:', amount_removed_symbols)


if __name__ == '__main__':
    test_all()
    main()
