from common import read_file


def first_negative(line: str) -> int:
    total = 0
    for i, symbol in enumerate(line, 1):
        total += (-1, 1)[symbol == '(']
        if total < 0:
            return i
    return 0


def test_all() -> None:
    line = '(()(()('
    assert line.count('(') - line.count(')') == 3
    assert first_negative(line) == 0
    line = '()())'
    assert first_negative(line) == 5


def main() -> None:
    name = 'data/01_input.txt'
    data = tuple(read_file(name))[0]
    print('Part one:', data.count('(') - data.count(')'))
    print('Part two:', first_negative(data))


if __name__ == '__main__':
    test_all()
    main()
