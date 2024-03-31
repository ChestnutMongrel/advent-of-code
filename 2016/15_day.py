from common import read_file, get_data, timer
import re


def test_all() -> None:
    data = read_file('data/15_example.txt')
    positions = parse_data(data)
    result = part_one(positions)
    correct = 5
    assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> dict:
    result = dict()
    number_pattern = re.compile(r'\d+')
    for line in data:
        # The line looks like this:
        # Disc #2 has 2 positions; at time=0, it is at position 1.
        numbers = tuple(map(int, number_pattern.findall(line)))
        result[numbers[0]] = (numbers[1], numbers[-1])
    return result


def part_one(data: dict) -> int:
    shift = current = 0
    for index, (positions, start) in data.items():
        if positions > shift:
            shift = positions
            current = (2 * shift - index - start) % shift

    while True:
        for index, (positions, start) in data.items():
            if not (current + index + start) % positions == 0:
                break
        else:
            return current
        current += shift


def main() -> None:
    data = parse_data(get_data(2016, 15))
    print('Part one:', part_one(data))
    # 121835 is too high
    # 121834 is the right one XD
    data[len(data) + 1] = (11, 0)
    print('Part two:', part_one(data))


if __name__ == '__main__':
    test_all()
    main()
