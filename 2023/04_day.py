"""
--- Day 4: Scratchcards ---
"""


from common import read_file


def get_cards(data: list) -> tuple:
    cards = list()
    for line in data:
        cards.append(line.split(': ')[1].split(' | '))
    return tuple(cards)


def win(winning: str, current: str) -> int:
    return len(set(winning.split()) & set(current.split()))


def points(data: tuple) -> int:
    if amount := win(*data):
        return 2 ** (amount - 1)
    return 0


def sum_points(data: tuple) -> int:
    return sum(points(item) for item in data)


def cards_amount(data: tuple) -> int:
    copies = dict()

    for num, game in enumerate(data,):
        value = copies.setdefault(num, 1)
        win_amount = win(*game)
        for i in range(1, win_amount + 1):
            copies[num + i] = copies.get(num + i, 1) + value

    return sum(copies.values())


def test_all() -> None:
    name = 'data/04_example.txt'
    data = get_cards(read_file(name))

    result = sum_points(data)
    correct = 13
    assert result == correct, f'Should be {correct}, get {result} instead.'

    result = cards_amount(data)
    correct = 30
    assert result == correct, f'Should be {correct}, get {result} instead.'


def main() -> None:
    data = get_cards(read_file('data/04_input.txt'))
    print('How many points?', sum_points(data))
    print('How many scratchcards?', cards_amount(data))


if __name__ == '__main__':
    test_all()
    main()
