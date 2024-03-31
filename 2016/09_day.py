from common import read_file, get_data


def test_part_one() -> None:
    check = (
        ('ADVENT', 6),
        ('A(1x5)BC', 7),
        ('(3x3)XYZ', 9),
        ('A(2x2)BCD(2x2)EFG', 11),
        ('(6x1)(1x3)A', 6),
        ('X(8x2)(3x3)ABCY', 18)
    )
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_part_two() -> None:
    check = (
        ('(3x3)XYZ', 9),
        ('X(8x2)(3x3)ABCY', 20),
        ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
        ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
    )
    for data, correct in check:
        result = part_two(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(line: str) -> int:
    before = after = 0
    current = 0
    while True:
        if (ind_st := line.find('(', current)) == -1:
            break

        ind_fin = line.find(')', ind_st)
        marker = line[ind_st + 1:ind_fin]

        amount, repeat = map(int, marker.split('x'))

        before += amount + ind_fin - ind_st + 1
        after += amount * repeat
        current = ind_fin + amount

    return len(line) - before + after


def part_two(line: str) -> int:
    # An example:
    # X(8x2)(3x3)ABCY

    new_len = 0

    index = 0
    while index < len(line):
        if line[index] != '(':
            new_len += 1

        else:
            ind_fin = line.find(')', index)
            marker = line[index + 1:ind_fin]
            amount, repeat = map(int, marker.split('x'))
            len_part = part_two(line[ind_fin + 1:ind_fin + 1 + amount])
            new_len += len_part * repeat
            index = ind_fin + amount

        index += 1

    return new_len


def main() -> None:
    data = get_data(2016, 9)[0]
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_part_one()
    test_part_two()
    main()
