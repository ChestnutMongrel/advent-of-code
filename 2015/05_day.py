from common import get_data
from itertools import pairwise


def test_all() -> None:
    check = (
        ('ugknbfddgicrmopn', True),
        ('aaa', True),
        ('jchzalrnumimnmhp', False),
        ('haegwjzuvuyypxyu', False),
        ('dvszwmarrgswjxmb', False)
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'

    check = (
        ('qjhvhtzxzqqjkmpb', True),
        ('xxyxx', True),
        ('uurcxstgmygtbstg', False),
        ('ieodomkazucvgmuy', False)
    )
    for data, correct in check:
        result = part_two(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: str) -> bool:
    not_nice = ('ab', 'cd', 'pq', 'xy')

    for item in not_nice:
        if item in data:
            return False

    vowels = 'aeiou'
    total_vowels = 0
    for letter in vowels:
        total_vowels += data.count(letter)
    if total_vowels < 3:
        return False

    for f, s in pairwise(data):
        if f == s:
            return True

    return False


def part_two(data: str) -> bool:
    # have_pair = False
    for x, y in pairwise(data):
        if data.count(x + y) > 1:
            break
    else:
        return False

    for i in range(0, len(data) - 2):
        if data[i] == data[i + 2]:
            return True

    return False


def main() -> None:
    print(sum(map(part_one, get_data(2015, 5))))
    print(sum(map(part_two, get_data(2015, 5))))


if __name__ == '__main__':
    test_all()
    main()
