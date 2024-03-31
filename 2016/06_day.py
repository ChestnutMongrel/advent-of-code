from common import read_file, get_data
from collections import Counter


def test_all() -> None:
    data = tuple(read_file('data/06_example.txt'))
    correct = 'easter'
    result = decode_repetition(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'
    correct = 'advent'
    result = decode_repetition(data, True)
    assert correct == result, f'Should be {correct}, got {result} instead.'


def decode_repetition(data: tuple, least_common: bool = False) -> str:
    result = ''
    for i in range(len(data[0])):
        letters = Counter((line[i] for line in data))
        letters = sorted(letters, key=lambda x: letters.get(x), reverse=not least_common)
        result += letters[0]
    return result


def main() -> None:
    data = get_data(2016, 6)
    print('Part one:', decode_repetition(data))
    print('Part two:', decode_repetition(data, least_common=True))


if __name__ == '__main__':
    test_all()
    main()
