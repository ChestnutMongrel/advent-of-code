from common import get_data


def test_create_dragon_curve() -> None:
    check = (
        ('1', '100'),
        ('0', '001'),
        ('11111', '11111000000'),
        ('111100001010', '1111000010100101011110000')
    )
    for data, correct in check:
        result = create_dragon_curve(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_create_checksum() -> None:
    check = (
        ('110010110100', '110101'),
        ('110101', '100')
    )
    for data, correct in check:
        result = create_checksum(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_one() -> None:
    result = part_one('10000', 20)
    correct = '01100'
    assert correct == result, f'In part_one should be {correct}, got {result} instead.'


def test_all() -> None:
    test_create_dragon_curve()
    test_create_checksum()
    test_part_one()


def create_dragon_curve(line: str) -> str:
    changed = ''.join(reversed(line)).replace('1', '2').replace('0', '1').replace('2', '0')
    return '0'.join((line, changed))


def create_checksum(line: str) -> str:
    checksum = ''
    for i in range(0, len(line), 2):
        first, second = line[i:i + 2]
        checksum += str(int(first == second))
    return checksum


def part_one(line: str, length: int) -> str:
    while len(line) < length:
        line = create_dragon_curve(line)

    checksum = line[:length]
    while checksum := create_checksum(checksum):
        if len(checksum) % 2 == 1:
            return checksum


def main() -> None:
    data = get_data(2016, 16)[0]
    length_one = 272
    length_two = 35651584
    print('Part one:', part_one(data, length_one))
    print('Part two:', part_one(data, length_two))


if __name__ == '__main__':
    test_all()
    main()
