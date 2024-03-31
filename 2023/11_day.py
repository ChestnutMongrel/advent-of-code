"""
--- Day 11: Cosmic Expansion ---
I really dislike inconsistency. Some functions returns lists when some creates generators...
"""


def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip()


def expand(universe: list) -> tuple:
    vertical = list()
    for i, line in enumerate(universe):
        if len(set(line)) == 1:
            vertical.append(i)
    horizontal = list(range(len(universe[0])))
    for line in universe:
        if '#' in line:
            for i, symbol in enumerate(line):
                if symbol == '#' and i in horizontal:
                    horizontal.remove(i)
    return tuple(vertical), tuple(horizontal)


def find_galaxies(universe: list) -> list:
    galaxies = list()
    for i, line in enumerate(universe):
        for ii, symbol in enumerate(line):
            if symbol == '#':
                galaxies.append((i, ii))
    return galaxies


def count_distances(galaxies: list, expansion: list, extra: int = 2) -> list:
    distances = list()
    for i, value in enumerate(galaxies[:-1]):
        f_x, f_y = value
        for s_x, s_y in galaxies[i+1:]:
            # should change distances instead of counting them this way
            distance_x = len(tuple(filter(lambda item: f_x < item < s_x or f_x > item > s_x, expansion[0]))) * (extra - 1)
            distance_y = len(tuple(filter(lambda item: f_y < item < s_y or f_y > item > s_y, expansion[1]))) * (extra - 1)
            distances.append(abs(f_x - s_x) + abs(f_y - s_y) + distance_x + distance_y)
    return distances


def main() -> None:

    for name in ('data/12_example.txt', 'data/11_input.txt'):
        # print(*expand(read_file(name)), sep='\n')
        universe = list(read_file(name))
        expantion = expand(universe)
        galaxies = find_galaxies(universe)
        distances = count_distances(galaxies, expantion, 1_000_000)

        # print(*universe, sep='\n')
        print(f'{galaxies = }')
        # print(f'{distances = }')
        # print(f'{expantion = }')
        print('sum all distances', sum(distances))


if __name__ == '__main__':
    main()
