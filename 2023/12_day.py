from common import read_file, timer
from itertools import combinations


def get_data(line: str, amount: int = 1) -> tuple:
    symbols, numbers = line.split()
    symbols = [symbols] * amount
    symbols = '?'.join(symbols)
    numbers = tuple((int(item) for item in numbers.split(','))) * amount
    return symbols, numbers


def get_indexes(line: str, symbol: str = '?') -> int:
    for i, letter in enumerate(line):
        if letter == symbol:
            yield i


def replace_by_index(line: str, new_symbol: str, index: int) -> str:
    return line[:index] + new_symbol + line[index+1:]


def len_groups(line: str) -> tuple:
    line = line.replace('.', ' ').replace('?', ' ').split()
    return tuple(map(len, line))


def first_part(symbols: str, numbers: tuple) -> int:

    damaged = symbols.count('#')
    unknown = symbols.count('?')
    total = sum(numbers)

    if damaged + unknown == total:
        return 1

    possible = 0
    for indexes in combinations(get_indexes(symbols), total - damaged):
        new_symbols = list(symbols)
        for i in indexes:
            new_symbols[i] = '#'
        new_symbols = ''.join(new_symbols)
        if len_groups(new_symbols) == numbers:
            possible += 1

    return possible


@timer
def get_sum(data: tuple) -> int:
    return sum(first_part(*item) for item in data)


def main() -> None:
    # First part is too slow...

    for name in ('data/12_example.txt', ):  # 'data/12_input.txt',):'data/example_12.txt',
        data = tuple(get_data(item) for item in read_file(name))
        # print(*data, sep='\n')
        total = get_sum(data)
        print(total)


if __name__ == '__main__':
    main()
