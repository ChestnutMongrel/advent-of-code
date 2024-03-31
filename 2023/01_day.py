"""
--- Day 1: Trebuchet?! ---
"""


from common import read_file


def test_all() -> None:
    name = 'data/01_example.1.txt'
    result_1 = count_sum(read_file(name))
    result_2 = count_sum(read_file(name), False)
    correct = 142
    assert result_1 == correct, f'Should be {correct}, get {result_1} instead.'
    assert result_2 == correct, f'Should be {correct}, get {result_2} instead.'

    name = 'data/01_example.2.txt'
    result_1 = count_sum(read_file(name))
    result_2 = count_sum(read_file(name), False)
    correct_1 = 209
    correct_2 = 281
    assert result_1 == correct_1, f'Should be {correct_1}, get {result_1} instead.'
    assert result_2 == correct_2, f'Should be {correct_2}, get {result_2} instead.'


def to_digits(line: str, digits: tuple) -> str:
    return line if line.isdigit() else str(digits.index(line) + 1)


def find_left_right_digits(line: str) -> str:
    start = finish = 0

    for letter in line:
        if letter.isdigit():
            finish = letter
            if not start:
                start = finish

    return start + finish


def word_to_number(line: str) -> str:
    digits = ('one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine')

    for num, digit in enumerate(digits, 1):
        repl_to = ''.join((digit, str(num), digit))
        line = line.replace(digit, repl_to)

    return line


def count_sum(data: tuple, only_digits: bool = True) -> int:
    if not only_digits:
        data = tuple(word_to_number(item) for item in data)
    return sum(int(find_left_right_digits(item)) for item in data)


def main() -> None:
    name = 'data/01_input.txt'
    print('Only digits count:', count_sum(read_file(name)))
    print('With words as digits:', count_sum(read_file(name), False))


if __name__ == '__main__':
    test_all()
    main()
