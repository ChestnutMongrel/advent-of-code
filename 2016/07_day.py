from common import get_data


def test_all() -> None:
    check = (
        ('abba[mnop]qrst', True),
        ('abcd[bddb]xyyx', False),
        ('aaaa[qwer]tyui', False),
        ('ioxxoj[asdfgh]zxcvbn', True)
    )
    for data, correct in check:
        result = is_suitable_abba(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'

    check = (
        ('aba[bab]xyz', True),
        ('xyx[xyx]xyx', False),
        ('aaa[kek]eke', True),
        ('zazbz[bzb]cdb', True),
    )
    for data, correct in check:
        result = is_suitable_bab(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def splitting(data: str) -> tuple:
    inside_brackets = list()
    outside_brackets = list()

    split_data = data.split('[')
    for line in split_data:
        if ']' in line:
            inside, outside = line.split(']')
            inside_brackets.append(inside)
            outside_brackets.append(outside)
        else:
            outside_brackets.append(line)

    return inside_brackets, outside_brackets


def is_contain_abba(line: str) -> bool:
    for i in range(len(line) - 3):
        first, second, third, fourth = line[i:i + 4]
        if first == fourth and second == third and first != second:
            return True
    return False


def find_bab(line: str) -> tuple:
    result = list()
    for i in range(len(line) - 2):
        first, second, third = line[i:i + 3]
        if first == third and first != second:
            result.append(line[i:i + 3])
    return tuple(result)


def is_suitable_abba(data: str) -> bool:
    inside, outside = splitting(data)

    for line in inside:
        if is_contain_abba(line):
            return False

    for line in outside:
        if is_contain_abba(line):
            return True

    return False


def is_suitable_bab(data: str) -> bool:
    inside, outside = splitting(data)
    set_inside = set()
    set_outside = set()
    for line in inside:
        for bab in find_bab(line):
            set_inside.add(bab[1:])
    for line in outside:
        for bab in find_bab(line):
            set_outside.add(bab[:-1])

    return bool(set_outside.intersection(set_inside))


def main() -> None:
    data = get_data(2016, 7)
    result_part_one = sum(map(is_suitable_abba, data))
    result_part_two = sum(map(is_suitable_bab, data))
    print('Part one:', result_part_one)
    print('Part two:', result_part_two)


if __name__ == '__main__':
    test_all()
    main()
