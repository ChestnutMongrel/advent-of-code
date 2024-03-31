"""
--- Day 3: Gear Ratios ---
"""


from common import read_file


def extract_numbers(line: str):
    line = line.split()

    for value in line:
        if value.isdigit():
            yield value

        else:
            for letter in value:
                if not letter.isdigit():
                    value = value.replace(letter, ' ')
            for item in extract_numbers(value):
                # print(item)
                yield item


def find_numbers_mul(lines: list) -> int:
    len_line = len(lines[0])
    num_lines = len(lines)
    total = 0
    close_to_symbol = dict()
    symbol = '*'

    for ind_line, line in enumerate(lines):

        start = 0
        numbers = dict()

        for number in extract_numbers(line):
            start += line[start:].find(number)
            numbers[start] = number
            start += len(number)

        for ind, number in numbers.items():
            ind_from = ind - 1 if ind else ind
            ind_to = ind + len(number)
            if ind_to < len_line:
                ind_to += 1

            if line[ind_from] == symbol:
                key = ind_line * len_line + ind_from
                close_to_symbol.setdefault(key, list()).append(number)

            if line[ind_to - 1] == symbol:
                key = ind_line * len_line + ind_to - 1
                close_to_symbol.setdefault(key, list()).append(number)

            if ind_line:
                for i, letter in enumerate(lines[ind_line - 1][ind_from:ind_to]):
                    if letter == symbol:
                        key = (ind_line - 1) * len_line + ind_from + i
                        close_to_symbol.setdefault(key, list()).append(number)

            if ind_line < num_lines - 1:
                for i, letter in enumerate(lines[ind_line + 1][ind_from:ind_to]):
                    if letter == symbol:
                        key = (ind_line + 1) * len_line + ind_from + i
                        close_to_symbol.setdefault(key, list()).append(number)

    for data in close_to_symbol.values():
        if len(data) == 2:
            total += int(data[0]) * int(data[1])

    return total


def find_numbers_sum(lines: list) -> int:
    len_line = len(lines[0])
    total = 0
    not_the_symbols = '0123456789 '

    for ind_line, line in enumerate(lines):

        for number in extract_numbers(line):

            ind = line.find(number)
            ind_from = ind - 1 if ind else ind
            ind_to = ind + len(number)
            if ind_to < len_line:
                ind_to += 1

            if line[ind_from] not in not_the_symbols or line[ind_to - 1] not in not_the_symbols:
                total += int(number)
                line = line.replace(number, ' ' * len(number), 1)
                continue

            is_symbol = False

            if ind_line:
                without_space = lines[ind_line - 1][ind_from : ind_to].replace(' ', '')
                if without_space and not without_space.isdigit():
                    is_symbol = True
            if ind_line < len(lines) - 1:
                without_space = lines[ind_line + 1][ind_from : ind_to].replace(' ', '')
                if without_space and not without_space.isdigit():
                    is_symbol = True

            if is_symbol:
                total += int(number)

            line = line.replace(number, ' ' * len(number), 1)

    return total


def test_all() -> None:
    data = '''333.3
...*.'''
    data = data.replace('.', ' ').split('\n')
    correct_sum = 336
    correct_mul = 999
    result_sum = find_numbers_sum(data)
    result_mul = find_numbers_mul(data)
    assert result_sum == correct_sum, f'Should be {correct_sum}, get {result_sum} instead.'
    assert result_mul == correct_mul, f'Should be {correct_mul}, get {result_mul} instead.'

    example = 'data/03_example.txt'
    data = tuple(item.replace('.', ' ') for item in read_file(example))
    correct_sum = 4361
    correct_mul = 467835
    result_sum = find_numbers_sum(data)
    result_mul = find_numbers_mul(data)
    assert result_sum == correct_sum, f'Should be {correct_sum}, get {result_sum} instead.'
    assert result_mul == correct_mul, f'Should be {correct_mul}, get {result_mul} instead.'


def main() -> None:

    input_name = 'data/03_input.txt'
    data = tuple(item.replace('.', ' ') for item in read_file(input_name))

    print('total sum', find_numbers_sum(data))
    print('total mul', find_numbers_mul(data))


if __name__ == '__main__':
    test_all()
    main()
