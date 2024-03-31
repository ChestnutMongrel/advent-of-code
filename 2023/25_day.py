from common import read_file


def get_data(data: list) -> list:
    data_dict = dict()
    all_items = set()
    for item in data:
        key, value = item.split(': ')
        value = tuple(value.split())
        data_dict[key] = value
        all_items.add(key)
        all_items.update(value)

    # Printing
    # for key, value in data_dict.items():
    #     print(f'{key}:', value)
    # print(*all_items)
    # print(len(all_items))

    name_num = {name: i for i, name in enumerate(all_items)}
    amount_items = len(all_items)
    matrix = [[0] * amount_items for _ in range(amount_items)]

    # Don I need a full matrix?
    for key, value in data_dict.items():
        x = name_num[key]
        for item in value:
            y = name_num[item]
            matrix[x][y] = matrix[y][x] = 1

    return matrix


def main() -> None:
    # There are so-called bridges in a spanning tree of a graph what might help me with this problem.
    name = 'data/12_example.txt'
    data = get_data(read_file(name))

    name = 'data/25_input.txt'
    data = get_data(read_file(name))


if __name__ == '__main__':
    main()
