"""
Day 7: Camel Cards
"""
from collections import Counter


def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while data := file.readline():
            cards, bid = data.split()
            yield cards, int(bid)


def order_label(data: str) -> int:
    order = 'AKQT98765432J'
    len_order = len(order)
    result = 0
    for i in data:
        result = order.index(i) + result * len_order
    return result


def get_type_index(data: str, joker: bool) -> int:
    order = ((5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1))

    if not joker:
        type_ = tuple(sorted(Counter(data).values(), reverse=True))
        return order.index(type_)

    var = set(data)
    best = 7
    for item in var:
        type_ = tuple(sorted(Counter(data.replace('J', item)).values(), reverse=True))
        ind = order.index(type_)
        if ind < best:
            best = ind
    return best


def ordering(data: list, joker: bool = False) -> list:
    groups = dict()
    for item in data:
        ind = get_type_index(item[0], joker)
        groups[ind] = groups.setdefault(ind, list())
        groups[ind].append(item)

    groups = {i: groups[i] for i in sorted(groups)}

    result = list()
    for value in groups.values():
        result.extend(sorted(value, key=lambda x: order_label(x[0])))
    return result


def main() -> None:
    array = list(read_file('data/07_input.txt'))
    ordered = tuple(reversed(ordering(array)))
    ordered_j = tuple(reversed(ordering(array, True)))

    result = 0
    for i, data in enumerate(ordered_j, start=1):
        result += i * data[1]
    print(result)


if __name__ == '__main__':
    main()
