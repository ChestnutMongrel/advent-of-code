from common import read_file, get_data, timer
from itertools import cycle


def test_all() -> None:
    check = (
        (5, 3),
        (100, 73),
        (1_000, 977),
        (10_000, 3617),
        (100_000, 68929),
    )
    for data, correct in check:
        print(f'for data {data:_}')
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'

    check = (
        (5, 2),
        (7, 5),
        (16, 7),
        (33, 6),
        (1_000, 271),
        (10_000, 3439),
        (100_000, 40951),
        (1_000_000, 28995)
    )
    for data, correct in check:
        print(f'for data {data:_}')
        result = part_two(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


@timer
def part_one(amount: int) -> int:
    players = [1] * amount
    last = None
    stealer = True
    while 1 in players:
        # print(f'{players = }')
        for i in range(len(players)):
            if players[i]:
                if stealer:
                    last = i
                else:
                    players[i] = 0
                stealer = not stealer

    return last + 1


def stealing(amount: int) -> int:
    pass


@timer
def part_two(amount: int) -> int:
    players = [*range(1, amount + 1)]
    index = 0
    while amount > 1:
        # print(players)
        # print(f'{amount = }')
        # print(f'{index = }')
        to_remove = (index + amount // 2) % amount
        # print(f'{to_remove = }')
        players.pop(to_remove)
        if to_remove > index:
            # print(players)
            index += 1
        amount -= 1
        index = index % amount
    return players[0]


def main() -> None:
    data = int(get_data(2016, 19)[0])
    # print(data)
    # print('Part one:', part_one(data))
    print('Part two:', part_two(data))
    # part_two took 4737.362090013994020 secs
    # This is literally a programming crime >_<


if __name__ == '__main__':
    test_all()
    main()
