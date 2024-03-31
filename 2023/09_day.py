"""
--- Day 9: Mirage Maintenance ---
"""


def read_file(file_name: str) -> str:
    with open(file_name, 'r') as file:
        while line := file.readline().strip():
            yield line


def str_to_num(data: str) -> list:
    for item in data.split():
        yield int(item)


def main() -> None:
    predicts_last = list()
    predicts_first = list()

    for line in read_file('data/12_example.txt'):
        current = list(str_to_num(line))
        lasts = current[-1]
        first = current[0]
        mult = 1

        while any(current):
            mult *= -1
            current = [current[i] - current[i-1] for i in range(1, len(current))]
            lasts += current[-1]
            first += current[0] * mult

        predicts_last.append(lasts)
        predicts_first.append(first)

    print(predicts_last)
    print(sum(predicts_last))
    print(predicts_first)
    print(sum(predicts_first))


if __name__ == '__main__':
    main()
