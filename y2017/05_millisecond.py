from common import get_data, timer


YEAR = 2017
DAY = 5


def test_all() -> None:
    data = list(map(int, '0 3  0  1  -3'.split()))
    check = (
        (part_one(data.copy()), 5),
        (part_one(data.copy(), True), 10)
    )
    for result, correct in check:
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


@timer
def part_one(data: list, extra_condition: bool = False) -> int:
    jumps = 0
    ind = 0
    amount = len(data)

    while ind < amount:
        offset = data[ind]
        if extra_condition and offset >= 3:
            data[ind] -= 1
        else:
            data[ind] += 1
        ind += offset
        jumps += 1

    return jumps


def main() -> None:
    data = list(map(int, get_data(year=YEAR, day=DAY)))
    print('Part one:', part_one(data.copy()))
    print('Part two:', part_one(data.copy(), True))


if __name__ == '__main__':
    test_all()
    main()
