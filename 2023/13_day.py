def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip()


def find_reflection(pattern: list, total: bool = True) -> int:

    for i in range(len(pattern[:-1])):
        if compare(pattern[i], pattern[i+1]) < 2:
            ii = i
            smudge = 0
            for j in range(i + 1, len(pattern)):
                if ii < 0:
                    continue  # This line is just for not making more checking like in else after for.
                smudge += compare(pattern[ii], pattern[j])
                if (total and smudge) or (not total and smudge >= 2):
                    break
                ii -= 1
            else:
                if (total and not smudge) or (not total and smudge == 1):
                    return i + 1
    return 0


def turn(pattern: list) -> list:
    new_pattern = list()
    for i in range(len(pattern[0])):
        new_line = ''.join(line[i] for line in pattern)
        new_pattern.append(new_line)
    return new_pattern


def count_reflections(pattern: list, total: bool = True) -> int:
    if num := find_reflection(pattern, total):
        return num * 100

    pattern = turn(pattern)
    if num := find_reflection(pattern, total):
        return num


def compare(first: str, second: str) -> int:
    not_equal = 0
    for f, s in zip(first, second):
        if f != s:
            not_equal += 1
    return not_equal


def main() -> None:

    for name in ('data/13_input.txt',):
        total = 0
        total_with_smudge = 0
        pattern = list()
        for line in read_file(name):
            if line:
                pattern.append(line)
            else:
                total += count_reflections(pattern)
                total_with_smudge += count_reflections(pattern, False)

                pattern = list()

        total += count_reflections(pattern)
        total_with_smudge += count_reflections(pattern, False)

        print(name)
        print(f'{total = }')
        print('with smudge = ', total_with_smudge)


if __name__ == '__main__':
    main()