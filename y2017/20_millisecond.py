from common import read_file, get_data
import re


YEAR = 2017
DAY = 20


def test_all() -> None:
    data = parse_data(read_file('data/20_example.txt'))
    print(data)
    check = ()
    for data, correct in check:
        result = part_one(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(data: tuple) -> tuple:
    # p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
    particles = list()
    pattern = re.compile(r'p=<(.+)>, v=<(.+)>, a=<(.+)>')
    for line in data:
        print(line)
        print(pattern.findall(line))


def part_one(data: tuple) -> None:
    pass


def main() -> None:
    data = get_data(year=YEAR, day=DAY)
    # parse_data(data)
    print('Part one:', part_one(data))
    # print('Part two:', )


if __name__ == '__main__':
    test_all()
    main()
