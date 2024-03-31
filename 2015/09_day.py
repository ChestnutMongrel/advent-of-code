from common import read_file, get_data
from itertools import permutations, pairwise


def test_all() -> None:
    data = read_file('data/09_example.txt')
    print(part_one(data))
    # for data, correct in check:
    #     result = part_one(data)
    #     assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: tuple) -> int:
    locations = list()
    matrix = dict()

    for line in data:
        pair, distance = line.split(' = ')
        first, second = pair.split(' to ')
        distance = int(distance)
        if first not in locations:
            locations.append(first)
        if second not in locations:
            locations.append(second)
        matrix.setdefault(first, list()).append((second, distance))
        # matrix.setdefault(second, list()).append((first, distance))

    for i, location in enumerate(locations):
        print(f'{i}: {location}')

    print(*matrix.items(), sep='\n')

    array = [[float('inf')] * len(locations) for _ in range(len(locations))]
    for from_, values in matrix.items():
        for to_, distance in values:
            i_f = locations.index(from_)
            i_t = locations.index(to_)
            array[i_f][i_t] = array[i_t][i_f] = distance
    # print(*array, sep='\n')

    shortest = float('inf')
    longest = 0
    for item in permutations(range(len(locations)), len(locations)):
        # print(item)
        path = sum(array[x][y] for x, y in pairwise(item))
        # print(f'{path = }')
        shortest = min(shortest, path)
        longest = max(longest, path)

    return shortest, longest


def main() -> None:
    data = get_data(2015, 9)
    print('Part one:', part_one(data))
    # print('Part two:', result)


if __name__ == '__main__':
    test_all()
    main()
