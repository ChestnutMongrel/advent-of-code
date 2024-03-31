from common import get_data
from collections import Counter


YEAR = 2017
DAY = 4


def test_all() -> None:
    test_is_no_repeat()
    test_is_not_anagrams()


def test_is_no_repeat() -> None:
    check = (
        ('aa bb cc dd ee', True),
        ('aa bb cc dd aa', False),
        ('aa bb cc dd aaa', True)
    )
    for data, correct in check:
        result = is_no_repeat(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_is_not_anagrams() -> None:
    check = (
        ('abcde fghij', True),
        ('abcde xyz ecdab', False),
        ('a ab abc abd abf abj', True),
        ('iiii oiii ooii oooi oooo', True),
        ('oiii ioii iioi iiio', False)
    )
    for data, correct in check:
        result = is_not_anagrams(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def is_no_repeat(line: str) -> bool:
    words = line.split()
    return len(set(words)) == len(words)


def is_not_anagrams(line: str) -> bool:
    words = line.split()
    letters = list()

    for word in words:
        counted = Counter(word)
        if counted in letters:
            return False
        letters.append(counted)

    return True


def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    print('Part one:', sum(map(is_no_repeat, data)))
    print('Part two:', sum(map(is_not_anagrams, data)))


if __name__ == '__main__':
    test_all()
    main()
