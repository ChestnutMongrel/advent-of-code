from common import read_file, get_data


def test_equal_start_length():
    check = (
        ('asd', 'fer', 0),
        ('asd', 'asdf', 3),
        ('asd', 'atf', 1),
        ('a', 'b', 0),
        ('', 'sdf', 0)
    )
    for *data, correct in check:
        result = equal_start_length(*data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_all() -> None:
    replacements, _ = extract_data(read_file('data/19_example.txt'))
    check = (
        ('HOH', 4),
        ('HOHOHO', 7)
    )
    for data, correct in check:
        result = part_one(replacements, data)
        assert correct == result, f'Should be {correct}, got {result} instead.'

    replacements['e'] = ['H', 'O']
    check = (
        ('HOH', 3),
        ('HOHOHO', 6)
    )
    for data, correct in check:
        result = part_two(replacements, data)
        assert correct == result, f'Should be {correct}, got {result} instead.'


def extract_data(data: tuple) -> tuple:
    replacements = dict()
    molecule = ''
    for line in data:
        if not line:
            continue
        if '=>' not in line:
            molecule = line
            break
        key, value = line.split(' => ')
        replacements.setdefault(key, list()).append(value)

    # print(f'{replacements = }')
    # print(f'{molecule = }')

    return replacements, molecule


def part_one(replacements: dict, molecule: str) -> int:
    return len(replace_results(replacements, molecule))


def replace_results(replacements: dict, molecule: str) -> tuple:
    result = set()
    for pattern, substitutions in replacements.items():
        if pattern not in molecule:
            continue
        for sub in substitutions:
            start = 0
            # It's not very wise to use this kind of loop...
            while (index := molecule.find(pattern, start)) >= 0:
                new_line = molecule[:index] + molecule[index:].replace(pattern, sub, 1)
                result.add(new_line)
                start = index + 1

    # print(molecule)
    # print(result)
    return tuple(result)


def replace_from(index: int, replacements: dict, line: str) -> tuple:
    lines = set()

    for pattern, substitutions in replacements.items():
        if line[index:].startswith(pattern):
            for sub in substitutions:
                new_line = line[:index] + sub + line[index + len(pattern):]
                lines.add(new_line)

    return lines


def replace_one(line: str, pattern: str, sub: str) -> tuple | None:
    if pattern not in line:
        return None

    results = set()

    for i in range(len(line)):
        if line[i:].startswith(pattern):
            new_line = line[:i] + sub + line[i + len(pattern):]
            results.add(new_line)

    return tuple(results)


def part_two(replacements: dict, molecule: str) -> int:
    print(f'{replacements = }')
    print(f'{molecule = }')

    results = {molecule}
    steps = 0
    while True:
        steps += 1
        new_lines = set()
        for line in results:
            # if line == 'e':
            #     return steps - 1

            for pattern, subs in replacements.items():
                if pattern == 'e':
                    if line in subs:
                        return steps
                    else:
                        continue

                for sub in subs:
                    if sub in line:
                        # print(f'{sub = }')
                        # print(f'{line = }')
                        result = replace_one(line, sub, pattern)
                        # print(f'{result = }')
                        new_lines.update(result)
                        # print(f'{new_lines = }')
        if new_lines:
            results = new_lines
            # print(f'{new_lines = }')

        input('\nEnter to continue...\n')


def equal_start_length(first: str, second: str):
    min_length = min(len(first), len(second))
    for i in range(min_length):
        if first[i] != second[i]:
            return i
    return min_length


def create_molecule(replacements: dict, molecule: str) -> int:
    line = 'e'
    pass


def main() -> None:
    data, molecule = extract_data(get_data(2015, 19))
    print('Part one:', part_one(data, molecule))
    print('Part two:', part_two(data, molecule))
    # print('Part two:', result)


if __name__ == '__main__':
    test_equal_start_length()
    test_all()
    main()
