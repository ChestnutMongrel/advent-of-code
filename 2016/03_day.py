from common import get_data


def test_is_triangle() -> None:
    check = (
        ((5, 10, 25), False),
        ((4, 4, 4), True),
        ((3, 4, 5), True)
    )
    for data, correct in check:
        result = is_triangle(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def is_triangle(sides: tuple) -> bool:
    *shortest, long = sorted(sides)
    return long < sum(shortest)


def parse_data(data: tuple) -> tuple:
    for line in data:
        line = line.split()
        yield tuple(map(int, line))


def how_many_triangles(data: tuple) -> int:
    return sum((is_triangle(line) for line in data))


def parse_data_vertical(data: tuple) -> tuple:
    for i in range(0, len(data), 3):
        first, second, third = map(str.split, data[i:i + 3])
        for ii in range(3):
            yield int(first[ii]), int(second[ii]), int(third[ii])


def main() -> None:
    data = tuple(get_data(2016, 3))
    print('Part one:', how_many_triangles(parse_data(data)))
    print('Part two:', how_many_triangles(parse_data_vertical(data)))


if __name__ == '__main__':
    test_is_triangle()
    main()
