from common import read_file, get_data
from re import sub, findall, compile


def test_all() -> None:
    data = tuple(read_file('data/08_example.txt'))
    result = sum(map(part_one, data))
    correct = 12
    assert correct == result, f'Should be {correct}, got {result} instead.'

    result = sum(map(part_two, data))
    correct = 19
    assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(line: str) -> int:
    substitutions = {
        compile(r'\\x[\da-f]{2}'): '|',
        compile(r'\\"'): '!',
        r'\\\\': '?'
    }

    full_len = len(line)
    new_line = line[1:-1]

    for pattern, subs in substitutions.items():
        new_line = sub(pattern, subs, new_line)

    new_len = len(new_line)

    return full_len - new_len


def part_two(line: str) -> int:
    initial_len = len(line)
    len_with_additions = len(line) + 2
    for symbol in ('"', '\\'):
        len_with_additions += line.count(symbol)

    return len_with_additions - initial_len


def main() -> None:
    data = tuple(get_data(2015, 8))
    print('Part one:', sum(map(part_one, data)))
    print('Part two:', sum(map(part_two, data)))


if __name__ == '__main__':
    test_all()
    main()
