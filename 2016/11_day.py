from common import read_file, get_data
import re


def test_all() -> None:
    data = parse_data(read_file('data/11_example.txt'))
    print(data)
    part_one(data)
    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: dict) -> int:
    current = 0
    floors = 4

    can_be_moved = list()
    generators = data[current]['G']
    microchips = data[current]['M']

    if current + 1 < floors:
        up = current + 1

        for gen in generators:
            if gen not in microchips and not data[up]['M'] - data[up]['G']:
                can_be_moved.append(('G', gen))

        for chip in microchips:
            if chip in data[up]['G']:
                can_be_moved.append(('M', chip))

        if not can_be_moved:
            can_be_moved = data[current]['G'] & data[current]['M']

    print(can_be_moved)

    return 0


def parse_data(data: tuple) -> dict:
    floors = dict()
    # names = ('first', 'second', 'third', 'fourth')
    generator = re.compile(r'a ([a-z]*) generator')
    microchip = re.compile(r'a ([a-z]*)-compatible microchip')

    for i, line in enumerate(data):
        floors[i] = dict()
        floors[i]['G'] = set(generator.findall(line))
        floors[i]['M'] = set(microchip.findall(line))

    return floors


def main() -> None:
    data = parse_data(get_data(2016, 11))
    print(data)
    print('Part one:', part_one(data))
    # print('Part two:', part_one())


if __name__ == '__main__':
    test_all()
    main()
