from common import read_file
from collections import defaultdict


def parse_data(data: tuple[str]) -> dict:
    result = defaultdict(set)
    for line in data:
        start, end = map(int, line.split('/'))
        result[start].add(end)
        result[end].add(start)
    return result


data = parse_data(read_file('y2017/data/24_example.txt'))
print(type(data))
data = dict(data)
print(type(data))
print(data)
