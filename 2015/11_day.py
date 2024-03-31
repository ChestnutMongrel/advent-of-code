from common import get_data
from itertools import pairwise
from string import ascii_lowercase


def test_is_allowed() -> None:
    check = (
        ('hijklmmn', False),
        ('abbceffg', False),
        ('abbcegjk', False),
        ('abcdffaa', True),
        ('ghjaabcc', True)
    )
    for data, correct in check:
        result = is_allowed(data)
        assert correct == result, f'For "{data}" should be "{correct}", got {result} instead.'


def test_next_password() -> None:
    check = (
        ('abcdefgh', 'abcdffaa'),
        ('ghijklmn', 'ghjaabcc')
    )
    for data, correct in check:
        result = next_password(data)
        assert correct == result, f'For "{data}" should be "{correct}", got {result} instead.'


def replace_excluded(line: str) -> str:
    replacements = {'i': 'j', 'o': 'p', 'l': 'm'}
    for letter, new_one in replacements.items():
        if letter in line:
            ind = line.index(letter)
            line = line[:ind] + new_one + 'a' * (len(line) - ind - 1)
            break
    return line


def incrementing(line: str) -> str:
    # A string with only 'z' will become a string the same length with only 'a'

    letters = list(line)
    index = len(letters) - 1
    while line[index] == 'z' and index >= 0:
        letters[index] = 'a'
        index -= 1

    if not index == -1:
        next_letter_ind = ascii_lowercase.index(line[index]) + 1
        letters[index] = ascii_lowercase[next_letter_ind]

    return ''.join(letters)


def next_password(line: str) -> str:
    next_line = incrementing(replace_excluded(line))
    while not is_allowed(next_line):
        next_line = incrementing(next_line)
    return next_line


def is_allowed(line: str) -> bool:
    excluded = ('i', 'o', 'l')
    for letter in excluded:
        if letter in line:
            return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(line) - 3):
        if line[i:i+3] in alphabet:
            break
    else:
        return False

    pair = ''
    for first, second in pairwise(line):
        if first == second:
            if pair and first not in pair:
                return True
            else:
                pair += first

    return False


def main() -> None:
    data = tuple(get_data(2015, 11))[0]
    result = next_password(data)
    print('Part one:', result)
    print('Part two:', next_password(result))


if __name__ == '__main__':
    test_is_allowed()
    test_next_password()
    main()
